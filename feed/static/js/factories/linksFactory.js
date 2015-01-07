peer_post.factory('LinkFactory', function ($http) {
    return {
        linksList: [],
        getLinks: function(callback) {
            $http.get('/api/v1/links')
                .success(function(response) {
                    callback(response);
                }).error(function (error) {
                    console.log(error);
                });
        }
    }
});
