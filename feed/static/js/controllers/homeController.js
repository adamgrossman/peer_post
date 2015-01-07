function homeController($scope, $http, GroupFactory, LinkFactory) {

//    GROUPS
//    Get groups
    GroupFactory.getGroups(function(response) {
        $scope.allGroups = response;
        GroupFactory.groupList = $scope.allGroups;
    });

//    LINKS
//    Get links
    LinkFactory.getLinks(function(response) {
        $scope.allLinks = response;
        LinkFactory.linksList = $scope.allLinks;
    });


}
