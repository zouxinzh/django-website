$(window).scroll(function(){
    var scroll = $(window).scrollTop();
    if(scroll < 300){
        $('.navbar').css('background', 'transparent');
    } else{
        $('.navbar').css('background', '#e12619');
    }
});