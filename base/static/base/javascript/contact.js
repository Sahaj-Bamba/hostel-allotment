$(document).ready(function(){
    var TP=0;
    $(".tag").hover(function(){

        $(this).children(".image").css("display","none");
        $(this).children(".image2").css("display","inline-block");
        } ,

        function(){
            $(this).children(".image2").css("display","none");
            $(this).children(".image").css("display","inline-block");
        }
    );
});
