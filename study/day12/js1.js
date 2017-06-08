/**
 * Created by xuzhen on 2017/6/7.
 */


function Foo(n) {
    this.name = n;

}
Foo.prototype = {
    "sysName":function () {
        console.log(this.name);
    }
};


var fo = new Foo("we");

fo.sysName();

// var obj = document.getElementById("id");
//
// obj.innerHTML = "<a href='#'> hahhfsfsd </a>";
// obj.innerText = "fsdf";
//
// obj.value = "eqw";
// obj.checked = true;

var obj = document.getElementsByClassName("i1")

// obj.style.fontSize
// obj.style.backgroundColor