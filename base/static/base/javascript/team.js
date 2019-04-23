$(document).ready(function () {
    var x=1;
    $(".cat").click(function(){
        if ($(this).children(".all_pro").css('display') == "none") {
            $(this).children(".all_pro").slideDown(100);
        }
        else{
            $(this).children(".all_pro").slideUp(1000);
        }
        x++;
    });
});
