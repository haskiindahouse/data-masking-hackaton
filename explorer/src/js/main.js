import * as bootstrap from 'bootstrap';

const route_initializers = {
    explorer_index:      () => import('./query-list').then(({setupQueryList}) => setupQueryList()),
    query_detail:        () => import('./explorer').then(({ExplorerEditor}) =>
        new ExplorerEditor(document.getElementById('queryIdGlobal').value)),
    query_create:        () => import('./explorer').then(({ExplorerEditor}) => new ExplorerEditor('new')),
    explorer_playground: () => import('./explorer').then(({ExplorerEditor}) => new ExplorerEditor('new')),
    explorer_schema:     () => import('./schema').then(({setupSchema}) => setupSchema()),
    explorer_connection_create:            () => import('./uploads').then(({setupUploads}) => setupUploads()),
    explorer_connection_update:            () => import('./uploads').then(({setupUploads}) => setupUploads())
};

document.addEventListener('DOMContentLoaded', function() {
    const clientRoute = document.getElementById('clientRoute').value;
    if (route_initializers.hasOwnProperty(clientRoute)) {
        route_initializers[clientRoute]();
    }
});
