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
        },

        newLink: function (data, callback) {
            $http.post('/api/v1/links/', data)
                .success(function (response) {
                    callback(response);
                })
                .error(function (error) {
                    console.log(error);
                });
        },

        action: function (link_id, action, callback) {
            var choice;

            if (action === 1) {
                choice = '/upvote/';
            }
            else if (action === 2) {
                choice = '/downvote/';
            }
            else if (action === 3) {
                choice = '/flag/';
            }

            $http.post('/api/v1/links/' + link_id + choice, {})
                .success(function (response) {
                    callback(response);
                })
                .error(function (error) {
                    console.log(error)
                })
        }
    }
});
