function PostsCtrlAjax($scope, $http)

{

$http({method: 'POST', url: 'js/posts.json'}).success(function(data) {
$scope.posts = data;
});

}
