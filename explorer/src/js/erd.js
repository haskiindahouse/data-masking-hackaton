import { fetchSchema, getConnElement } from './schemaService.js';

document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM fully loaded and parsed');

    function updateSchema() {
        console.log('updateSchema called');
        fetchSchema().then(schema => {
            console.log('Schema received:', schema);
            window.editor.dispatch({
                effects: StateEffect.appendConfig.of(
                    StandardSQL.language.data.of({
                        autocomplete: schemaCompletionSource({ schema: schema })
                    })
                )
            });
            drawDiagram(schema);
        });

        document.querySelector("#schema_frame").setAttribute("src", `../schema/${getConnElement().value}`);
    }

    function drawDiagram(schema) {
        console.log('drawDiagram called with schema:', schema);
        const $ = go.GraphObject.make;

        const myDiagram = $(go.Diagram, "diagramDiv", {
            "undoManager.isEnabled": true
        });

        myDiagram.nodeTemplate = $(go.Node, "Auto",
            $(go.Shape, "RoundedRectangle",
                { strokeWidth: 0, fill: "white" },
                new go.Binding("fill", "color")),
            $(go.TextBlock,
                { margin: 8, font: "bold 14px sans-serif", stroke: '#333' },
                new go.Binding("text", "key"))
        );

        const nodeDataArray = [];
        const linkDataArray = [];

        if (schema.tables) {
            schema.tables.forEach(table => {
                nodeDataArray.push({ key: table.name, color: "lightblue" });

                table.foreign_keys.forEach(fk => {
                    linkDataArray.push({ from: table.name, to: fk.references });
                });
            });
        }

        myDiagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);
    }

    document.querySelector('#sql_accordion_1').addEventListener('shown.bs.collapse', function () {
        console.log('Accordion expanded');
        updateSchema();
    });
});
