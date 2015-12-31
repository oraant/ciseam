//将一个列表构建成表头并返回
function getThead(list){
    var thead = document.createElement("thead");
    var tr = document.createElement("tr");
    for (i in list){
        th = document.createElement("th");
        text = document.createTextNode(list[i]);
        th.appendChild(text);
        tr.appendChild(th);
        }
    thead.appendChild(tr)
    return thead;
    }

//将一个二维数组构建成表体并返回
function getTbody(list){
    var tbody = document.createElement("tbody");
    for (i in list){
        tr = document.createElement("tr");
        for (x in list[i]){
            td = document.createElement("td");
            text = document.createTextNode(list[i][x]);
            td.appendChild(text);
            tr.appendChild(td);
            }
        tbody.appendChild(tr);
        }
    return tbody;
    }

function fillTable(table,headlist,bodylist){
    var thead = getThead(headlist);
    var tbody = getTbody(bodylist);
    table.appendChild(thead);
    table.appendChild(tbody);
    }
