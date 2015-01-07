var peer_post = angular.module('peer_post', ['ngRoute', 'ui.bootstrap']);

peer_post.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: '/static/js/views/home.html',
            controller: homeController
        })
        .otherwise({redirectTo: '/'});
}]);
