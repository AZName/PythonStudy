/**
 * Created by xuzhen on 2017/6/5.
 */


function func() {

    var tag = document.getElementById("i1");
    var content = tag.innerText;
    var i = content.charAt(0);
    var old = content.substring(1,content.length);
    var new_tag = old + i;
    tag.innerText = new_tag;

}

setInterval("func()",500)