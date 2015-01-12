peer_post.directive('button', function () {
    return {
        restrict: 'E',
        compile: function(element, attributes) {
            element.addClass('btn');
            if (attributes.type == 'submit') {
                element.addClass('btn-success');
            }
            else if (attributes.type == 'submit-main') {
                element.addClass('btn-success submit-main');
            }
            if (attributes.size) {
                element.addClass('btn-' + attributes.size);
                element.addClass('btn-block');
            }
        }
    }
});

//<submit-button class="btn-xs" ng-click="newGroup()">Submit</submit-button>