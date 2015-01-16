function homeController($scope, GroupFactory, LinkFactory) {

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
    function get_links() {
        LinkFactory.getLinks(function(response) {
            $scope.allLinks = response;
            LinkFactory.linksList = $scope.allLinks;
        });
    }

    get_links();

//    Create link
    $scope.newLink = function () {
        //    Logged in user id
        var logged_user = document.getElementById('logged_id').innerHTML;

        var data = {
            "url": $scope.newLinkUrl,
            "title": $scope.newLinkTitle,
            "description": $scope.newLinkDesc,
            "group": $scope.newLinkGroup.id,
            "posted_user": logged_user
        };

        LinkFactory.newLink(data, function(response) {
            $scope.allLinks.push(response);
            LinkFactory.linksList = $scope.allLinks;
        });

        $scope.createNewLink = false;
    };

    $scope.upVote = function (link) {
        var link_id = link.id;
        LinkFactory.action(link_id, 1, function() {
            get_links();
        });
    };

    $scope.downVote = function (link) {
        var link_id = link.id;
        LinkFactory.action(link_id, 2, function() {
            get_links();
        });
    };

    $scope.flag = function (link) {
        var link_id = link.id;
        LinkFactory.action(link_id, 3, function() {
            get_links();
        });
    };
}
