var point = [];
var x1 = 0, y1 = 0, x2 = 0, y2 = 0;
var x, y, w, h;
var xp, yp, wp, hp;
var value_rect;
var w_margin = 50;
var h_margin = 80;
var drawWidth = 3;
var id = 0;
var k = 0;
var begin_ev = "indefinite";
var after = [];
var rectValue = [];
var duration = "3s"


function action_coords(event) {
    var x_value = event.clientX;
    var y_value = event.clientY;
    if (x1 == 0) {
        x1 = x_value;
        y1 = y_value;
    }
    else {
        x2 = x_value;
        y2 = y_value;
    }

    if (x2 != 0) {
        if (x1>x2){
            var temp = x1;
            x1 = x2;
            x2 = temp;
        }
        if (y1>y2){
            var temp = y1;
            y1 = y2;
            y2 = temp;
        }
        value_rect = [x1-w_margin,y1-h_margin,x2-w_margin,y2-h_margin];
        send_xy();
        x = x1-w_margin, y = y1-h_margin, w = x2-x1, h = y2-y1;
        point.push([x, y, w, h]);
        rectangle = rect_html(x,y,w,h,id);
        svg_rect(rectangle);
        x1 = 0, x2 = 0, y1 = 0, y2 = 0, id++;
    }
}
function rect_html(x,y,w,h,id){

    var rectangle = document.createElementNS("http://www.w3.org/2000/svg", 'rect');
    rectangle.setAttribute("id", "rect_" + id);
    rectangle.setAttribute("x", x);
    rectangle.setAttribute("y", y);
    rectangle.setAttribute("width", w);
    rectangle.setAttribute("height", h);
    rectangle.setAttribute("class", "svgObject");
    rectangle.setAttribute("drawtype", "rectangle");
    rectangle.setAttribute("fill", "#00ff00");
    rectangle.setAttribute("stroke-width", "2px");
    rectangle.setAttribute("stroke", "#00FF00");
    return rectangle;
}

function svg_rect(rectangle){
    var rect = document.getElementById("rect");
    rect.append(rectangle);
}
function go(){
    magic();
    var elements = document.getElementsByTagName("animate");
    for (var i = 0; i < elements.length; i++) {
        elements[i].beginElement();
    }
    setTimeout(function(){
        end_rect();
    },3000);
}

function send_xy(){
        $.ajax({
            type : 'POST',
            url : '/easy_work',
            contentType :"application/json; charset=UTF-8",
            data : JSON.stringify({xy_group:value_rect}),
            dataType : 'json',
            success : function(result){
                rectValue.push(result.xy_point);
                after.push(result.xy_point);
                $("#message").html("<h1>Click!!</h1>");

            },
            error : function(xtr,status,error){
                    alert(xtr +":"+status+":"+error);
            }
       });
}
function magic(){
    for(var i in rectValue){
        x = rectValue[i][0], y = rectValue[i][1], w = rectValue[i][2], h = rectValue[i][3];
        xp = point[i][0], yp = point[i][1], wp = point[i][2], hp = point[i][3];
        var rect_id = "rect_" + k;

        var animate1 = document.createElementNS("http://www.w3.org/2000/svg", 'animate');
        animate1.setAttribute("attributeName", "x");
        animate1.setAttribute("attributeType", "xml");
        animate1.setAttribute("begin", begin_ev);
        animate1.setAttribute("dur", duration);
        animate1.setAttribute("fill", "freeze");
        animate1.setAttribute("from", xp);
        animate1.setAttribute("to", x);
        var animate2 = document.createElementNS("http://www.w3.org/2000/svg", 'animate');
        animate2.setAttribute("attributeName", "y");
        animate2.setAttribute("attributeType", "xml");
        animate2.setAttribute("begin", begin_ev);
        animate2.setAttribute("dur", duration);
        animate2.setAttribute("fill", "freeze");
        animate2.setAttribute("from", yp);
        animate2.setAttribute("to", y);
        var animate3 = document.createElementNS("http://www.w3.org/2000/svg", 'animate');
        animate3.setAttribute("attributeName", "width");
        animate3.setAttribute("attributeType", "xml");
        animate3.setAttribute("begin", begin_ev);
        animate3.setAttribute("dur", duration);
        animate3.setAttribute("fill", "freeze");
        animate3.setAttribute("from", wp);
        animate3.setAttribute("to", w);
        var animate4 = document.createElementNS("http://www.w3.org/2000/svg", 'animate');
        animate4.setAttribute("attributeName", "height");
        animate4.setAttribute("attributeType", "xml");
        animate4.setAttribute("begin", begin_ev);
        animate4.setAttribute("dur", duration);
        animate4.setAttribute("fill", "freeze");
        animate4.setAttribute("from", hp);
        animate4.setAttribute("to", h);

        var animate = document.getElementById(rect_id);
        console.log(animate);
        animate.append(animate1);
        animate.append(animate2);
        animate.append(animate3);
        animate.append(animate4);
        k++;
    }
    rectValue = [];
    point = [];
}
function end_rect(){
    $("#rect").empty();
    var rect = document.getElementById("rect");
    for(var i in after){
        x = after[i][0], y = after[i][1], w = after[i][2], h = after[i][3];
        var rectangle = document.createElementNS("http://www.w3.org/2000/svg", 'rect');
        rectangle.setAttribute("x", x);
        rectangle.setAttribute("y", y);
        rectangle.setAttribute("width", w);
        rectangle.setAttribute("height", h);
        rectangle.setAttribute("class", "svgObject");
        rectangle.setAttribute("drawtype", "rectangle");
        rectangle.setAttribute("fill", "#00ff00");
        rectangle.setAttribute("stroke-width", "2px");
        rectangle.setAttribute("stroke", "#00FF00");

        rect.append(rectangle);
    }

}


                    /*
                    console.log("x="+x+",y="+y+",w="+w+",h="+h+",xp="+xp+",yp="+yp);
                    $(rect_id).css("left", xp).css("top", yp).animate({
                        top: y
                    }, 500).animate({
                        left: x
                    }, 500).animate({
                        width: w
                        , height: h
                    }, 500);
                    */
/*

*/