/**
 * Created by pxxgogo on 2017/3/26.
 */


function search(obj) {
    var text = $("#search-input").val();
    $("#show-search-result-btn").attr("class", 'bg-primary');
    $.ajax({
        type: 'get',
        url: "/search_authors",
        data: {'domain': text},
        datatype: "json",
        // timeout: time,
        beforeSend: function () {
        },
        success: function (ret) {
            // console.log(ret);
            var tbody_html = "";
            var authors = ret.authors;
            if (authors.length == 0) {
                tbody_html = "Not Found!";
                alert(tbody_html);
                return;
            }
            for (var i = 0; i < authors.length; i++) {
                var index = authors[i].index;
                var info = authors[i].info;
                var name = info.name;
                var address = info.place;
                var cn = info.cn;
                var hi = info.hi;
                var pc = info.pc;
                var pi = info.pi;
                var upi = info.upi;
                tbody_html += "<tr id='t-a-" + index + "' class='author-row' onclick='get_coauthors(this)'>" +
                    "<td>" + (i + 1) + "</td>" +
                    "<td>" + name + "</td>" +
                    "<td>" + address + "</td>" +
                    "<td>" + hi + "</td>" +
                    "<td>" + pc + "</td>" +
                    "<td>" + cn + "</td>" +
                    "<td>" + pi + "</td>" +
                    "<td>" + upi + "</td>" +
                    "</tr>"
            }
            $("#authors-tbody").html(tbody_html);
            $('html, body').stop().animate({
                scrollTop: $("#search-result-section").offset().top
            }, 1500, 'easeInOutExpo');

        }
    });
}

// $(document).ready(function () {
//
//     $(".author-row").click(function () {
//
//     });
// });

function get_coauthors(obj) {
    var author_index = obj.id.substring(4);
    $.ajax({
        type: 'get',
        url: "/search_coauthors",
        data: {'id': author_index},
        datatype: "json",
        // timeout: time,
        beforeSend: function () {
        },
        success: function (ret) {
            console.log(ret);
            var tbody_html = "";
            var authors = ret.authors;
            if (authors.length == 0) {
                tbody_html = "Not Found!";
                alert(tbody_html);
                return;
            }
            for (var i = 0; i < authors.length; i++) {
                var index = authors[i].index;
                var times = authors[i].times;
                var info = authors[i].info;
                var name = info.name;
                var address = info.place;
                var cn = info.cn;
                var hi = info.hi;
                var pc = info.pc;
                var pi = info.pi;
                var upi = info.upi;
                tbody_html += "<tr id='t-a-" + index + "' class='author-row'>" +
                    "<td>" + (i + 1) + "</td>" +
                    "<td>" + name + "</td>" +
                    "<td>" + times + "</td>" +
                    "<td>" + address + "</td>" +
                    "<td>" + hi + "</td>" +
                    "<td>" + pc + "</td>" +
                    "<td>" + cn + "</td>" +
                    "<td>" + pi + "</td>" +
                    "<td>" + upi + "</td>" +
                    "</tr>"
            }
            $("#coauthors-tbody").html(tbody_html);
            $("#show-coauthors-btn").click();
        }
    });


}