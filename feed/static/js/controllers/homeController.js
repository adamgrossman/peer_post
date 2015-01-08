function homeController($scope, $http, GroupFactory, LinkFactory, $cookieStore) {

//    var current = user.current;
    console.log(logged_in_user);

//    GROUPS
//    Get groups
    GroupFactory.getGroups(function(response) {
        $scope.allGroups = response;
        GroupFactory.groupList = $scope.allGroups;
    });

//    Create group
    $scope.newGroup = function() {

        var data = {
            "title": $scope.newGroupName,
            "description": $scope.newGroupDesc
        };

        GroupFactory.newGroup(data, function(response) {
            $scope.allGroups.push(response);
            GroupFactory.groupList = $scope.allGroups;
        });

        $scope.createNewGroup = false;
    };


//    LINKS
//    Get links
    LinkFactory.getLinks(function(response) {
        $scope.allLinks = response;
        LinkFactory.linksList = $scope.allLinks;
    });

//    Create link
    $scope.newLink = function () {

        var group_id = $scope.newLinkGroup.id;
        console.log(group_id);

        var data = {
            "url": $scope.newLinkUrl,
            "title": $scope.newLinkTitle,
            "description": $scope.newLinkDesc,
            "group": group_id
//            "group": group_id,
//            "posted_user": 3
        };

        LinkFactory.newLink(data, function(response) {
            $scope.allLinks.push(response);
            LinkFactory.linksList = $scope.allLinks;
        })
    }

}
