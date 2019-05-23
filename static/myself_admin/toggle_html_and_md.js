$(document).ready(function(){
    var $text_md = $(".field-text");
    var $text_html = $(".field-text_html");
    var $is_md = $("#id_is_md");

    var toggle_html_and_md = function(is_md){
        if (is_md){
            $text_md.show();
            $text_html.hide();
        } else {
            $text_md.hide();
            $text_html.show();
        }
    };

    $is_md.click(function(){
        toggle_html_and_md($(this).is(":checked"));
    });

    setTimeout(function(){toggle_html_and_md($is_md.is(":checked"))}, 1000);  // 如果不延迟 > 0.5s，加载的 mdeditor 有问题
});
