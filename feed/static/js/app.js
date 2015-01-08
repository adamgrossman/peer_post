var peer_post = angular.module('peer_post', ['ngRoute', 'ngCookies', 'ui.bootstrap']).run(function ($http, $cookies) {
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
});

peer_post.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: '/static/js/views/home.html',
            controller: homeController
        })
        .otherwise({redirectTo: '/'});
}]);
