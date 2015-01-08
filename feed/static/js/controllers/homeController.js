function homeController($scope, $http, GroupFactory, LinkFactory) {

//    Logged in user
    var logged_user = document.getElementById('logged_id').innerHTML;

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
            "group": group_id,
            "posted_user": logged_user
        };

        LinkFactory.newLink(data, function(response) {
            $scope.allLinks.push(response);
            LinkFactory.linksList = $scope.allLinks;
        });

        $scope.createNewLink = false;
    }
}
