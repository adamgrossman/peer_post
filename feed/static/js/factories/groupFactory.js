peer_post.factory('GroupFactory', function ($http) {
    return {
        groupList: [],

        getGroups: function(callback) {
            $http.get('/api/v1/groups/')
                .success(function (response) {
                    callback(response);
                }).
                error(function(error) {
                    console.log(error);
                });
        },

        newGroup: function (data, callback) {
            $http.post('/api/v1/groups/', data)
                .success(function (response) {
                    callback(response);
                })
                .error(function (error) {
                    console.log(error);
                });
        }
    }
});
