const apiUrl = 'http://127.0.0.1:5000/';

var myApp = angular.module('myApp', ['ngResource', 'angularFileUpload']);

myApp.controller('MainController', function ($scope) {
    $scope.msg = "Test message";
});