var app = angular.module('pimoteApp', []);

app.controller('ChannelController', function($scope, $http){
    $http.get('/api/channel/').success(function(data){
        $scope.Channels = data.channels
    })

    $scope.showHours = function(){
        var d = new Date().getHours()
        return [d - 1 < 0 ? 23 : d - 1, d, d + 1 % 24, d + 2 % 24, d + 3 % 24]
    }


    $scope.getShowWidth = function(show){
        var start = new Date(show.startTime),
            end = new Date(show.endTime),
            viewportStart = new Date()
            minutePx = 500 / 60,
            width = ((end - start) / 1000 / 60) * minutePx,
            offset = 0;

        if((viewportStart.getHours() - 1) > start.getHours()){
          var clampedTime = viewportStart.setMinutes(0) - (viewportStart.getTime() - viewportStart.setSeconds(0)) - (1000 * 60 * 60)
          offset = ((start - clampedTime) / 1000 / 60) * minutePx;
        }
        return 'width: ' + Math.min((Math.floor(width) + Math.floor(offset)), 2500) + 'px;';
    }
}).directive('show', function(){
    return {
        template:'<div class="schedule-show-title text-ellipsis">{{ show.title }}</div><div class="text-ellipsis">{{ show.startTime | date: "HH:mm a" }} - {{ show.endTime | date: "HH:mm a" }}</div>'
    }
}).filter('nowFilter', function(){
    return function(input){
        var filterList = []
        angular.forEach(input, function(show, i, shows){
          if(new Date(show.startTime).getTime() >= (new Date().setMinutes(0)) - (1000 * 60 * 60) ||
             new Date(show.endTime).getTime() >= (new Date().setMinutes(0)) - (1000 * 60 * 60)) {
            filterList.push(show)
          }
        })
        return filterList.sort(function(show1, show2){
            return (new Date(show1.startTime)) > (new Date(show2.startTime))
        })
    }
})

app.controller('SidenavController', function($scope){
    $scope.toggleMenu = function(){
        $('.sidebar-wrapper').add('.wrapper').toggleClass('active')
    }
})