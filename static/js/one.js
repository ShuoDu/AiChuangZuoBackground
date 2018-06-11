var a =123;
var b= ' 欢迎来到爱创作网站'; //变量
/*
* 和ios中一样的
* */
// 单行注释
//5种基本数据类型：
//number、string、boolean、undefined、null
function tell() {
    alert(b)
}
tell();
// 获取元素
var odiv = document.getElementById('div1');
var typ = odiv.type;
var value = odiv.value;
odiv.style.color = 'red';

var oDiv = document.getElementById('div1');
        // //读取
        // var txt = oDiv.innerHTML;
        // alert(txt);
        //写入
oDiv.innerHTML = '<a href="http://www.baidu.cn">爱创作<a/>';

//匿名函数
window.onload = function(){
    var oBtn = document.getElementById('btn1');
    /*
    oBtn.onclick = myalert;
    function myalert(){
        alert('ok!');
    }
    */
    // 直接将匿名函数赋值给绑定的事件

    oBtn.onclick = function (){
        var cc = 9;
        if (cc == 9){
            alert("你的岁数不大啊%d", cc)
        }
    }
}
var aList = new Array(1,2,3);
var blist = [12,32,'23323'];
alert(blist.length)
blist.reverse(); //数组反转
var mlist = [[2,32,32],[23322323,56]];

console.log();
//定时器
var time1 = setTimeout(myalert,2000);
var time2 = setInterval(myalert,2000);
/*
clearTimeout(time1);
clearInterval(time2);
*/
function myalert(){
    alert('ok!');
}

// 封闭函数  一开始就执行的匿名函数
(function(){
    var oDiv = document.getElementById('div1');
    oDiv.style.color = 'red';
})();

/*
 闭包
  */

// 什么是闭包
// 函数嵌套函数，内部函数可以引用外部函数的参数和变量，参数和变量不会被垃圾回收机制收回

function aaa(a){
      var b = 5;
      function bbb(){
           a++;
           b++;
         alert(a);
         alert(b);
      }
      return bbb;
  }

 var ccc = aaa(2);

 ccc();
 ccc();

//面向对象
var Tom = {
    name : 'tom',
    age : 18,
    showname : function(){
        alert('我的名字叫'+this.name);
    },
    showage : function(){
        alert('我今年'+this.age+'岁');
    }
}