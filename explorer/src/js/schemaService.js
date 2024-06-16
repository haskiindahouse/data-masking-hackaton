const schemaCache = {};

const fetchSchema = async () => {
    const conn = getConnElement().value;

    if (schemaCache[conn]) {
        return schemaCache[conn];
    }

    try {
        const response = await fetch(`../schema.json/${conn}`);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const schema = await response.json();
        schemaCache[conn] = schema;  // Cache the schema
        return schema;
    } catch (error) {
        console.error('Error fetching table schema:', error);
        throw error;  // Re-throw to handle it in the calling function
    }
};

export const SchemaSvc = {
    get: fetchSchema
};

export function getConnElement() {
    return document.querySelector('#id_connection');
}

export async function drawERD() {
    console.log("DRAW ERD CALLED")
    try {
        const schema = await SchemaSvc.get();
        initDiagram(schema);
    } catch (error) {
        console.error('Error drawing ERD:', error);
    }
}

function initDiagram(schema) {
    const $ = go.GraphObject.make;

    const myDiagram = $(go.Diagram, "myDiagramDiv",
        {
            "undoManager.isEnabled": true
        });

    myDiagram.nodeTemplate =
        $(go.Node, "Auto",
            $(go.Shape, "RoundedRectangle", { strokeWidth: 0 },
                new go.Binding("fill", "color")),
            $(go.TextBlock, { margin: 8, font: "bold 12pt sans-serif" },
                new go.Binding("text", "name"))
        );

    const nodeDataArray = schema.tables.map(table => ({
        key: table.name,
        name: table.name,
        color: "lightblue"
    }));

    const linkDataArray = schema.relationships.map(rel => ({
        from: rel.from,
        to: rel.to
    }));

    myDiagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);
}
