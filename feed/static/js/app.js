var feed = angular.module('peer_post', ['ngRoute', 'ui.bootstrap']);

feed.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: '/static/js/views/home.html',
            controller: homeController
        })
}]);
