$(document).ready(function () {
  $('#example').DataTable();

  // $('.sidebar-left >.nav-item').click(function () {
  //   $(".sidebar-left >.nav-item").removeClass("active");
  //   $(this).addClass("active");
  // });

});

$(function () {

  $("#grid").jsGrid({
    width: "100%",
    height: "auto",
    // filtering: true,
    inserting: true,
    // editing: true,
    sorting: true,
    paging: true,
    autoload: true,
    data: clients,
    pageSize: 5,
    pageButtonCount: 5,

    deleteConfirm: "Do you really want to delete the client?",

    // controller: db,
    fields: [{
        name: "Id",
        type: "number",
        width: 50
      },
      {
        name: "Image",
        type: "text",
        width: 100
      },
      {
        name: "Name",
        type: "text",
        width: 100
      },
      Priorities,
      {
        name: "Cool",
        type: "checkbox",
        width: 40,
        title: "Is Active",
        sorting: false
      },
      {
        name:"edit",
        type:"button",
        sorting: false
      },
      {
        type: "control"
      }
    ],
    editValue: function() {
     alert("edit");
  },
    onItemEditing: function(args) {
      // cancel editing of the row of item with field 'ID' = 0
    alert(args.item.Id);
  }
  //   loadData: function(filter) {
  //     return $.ajax({
  //         type: "GET",
  //         url: "/items",
  //         data: filter
  //     });
  // },
  
  // insertItem: function(item) {
  //     return $.ajax({
  //         type: "POST",
  //         url: "/items",
  //         data: item
  //     });
  // },
  
  // updateItem: function(item) {
  //     return $.ajax({
  //         type: "PUT",
  //         url: "/items",
  //         data: item
  //     });
  // },
  
  // deleteItem: function(item) {
  //     return $.ajax({
  //         type: "DELETE",
  //         url: "/items",
  //         data: item
  //     });
  // },
  })
})

var clients = [{
    Id: 1,
    Image: "<img src='https://pos.ultimatefosters.com/uploads/img/1528727793_acerE15.jpg'>",
    Name: "Ada Love",
    Priority: 0,
    Cool: true,
  },
  {
    Id: 2,
    Image: "<img src='https://pos.ultimatefosters.com/uploads/img/1528780234_apples.jpg'>",
    Name: "Grace Hopper",
    Priority: 1,
    Cool: true,
  },
  {
    Id: 3,
    Image: "<img src='https://pos.ultimatefosters.com/uploads/img/1528727817_iphone8.jpg'>",
    Name: "Alan Turing",
    Priority: 2,
    Cool: true,
  },
  {
    Id: 4,
    Image: "<img src='https://pos.ultimatefosters.com/uploads/img/1528727849_macbookair.jpg'>",
    Name: "Miguel Alcubierre",
    Priority: 3,
    Cool: true,
  },
  {
    Id: 5,
    Image: "<img src='https://pos.ultimatefosters.com/uploads/img/1528727865_barilla_pasta.jpeg'>",
    Name: "Ada Lovelace",
    Priority: 4,
    Cool: true,
  }, {
    Id: 6,
    Image: "<img src='https://pos.ultimatefosters.com/uploads/img/1528727881_butter_cookies.jpg'>",
    Name: "Grace Hopper",
    Priority: 5,
    Cool: true,
  }, {
    Id: 7,
    Image: "<img src='https://pos.ultimatefosters.com/uploads/img/1528727917_diary_of_whimp_kid.jpeg'>",
    Name: "Alan Turing",
    Priority: 0,
    Cool: true,
  }, {
    Id: 8,
    Image: "<img src='https://pos.ultimatefosters.com/uploads/img/1528727999_lipton_tea.jpg'>",
    Name: "Miguel Alcubierre",
    Priority: 1,
    Cool: true,
  },
  {
    Id: 9,
    Image: "<img src='https://pos.ultimatefosters.com/uploads/img/1528728111_oreo.jpg'>",
    Name: "Ada Lovelace",
    Priority: 2,
    Cool: true,
  }, {
    Id: 10,
    Image: "<img src='https://pos.ultimatefosters.com/uploads/img/1528780470_eggs.jpg'>",
    Name: "Grace Hopper",
    Priority: 3,
    Cool: true,
  },
];

var Priorities = {
  name: "Priority",
  type: "select",
  items: [{
      Name: "India",
      Id: 0,
    },
    {
      Name: "United States",
      Id: 1
    },
    {
      Name: "France",
      Id: 2
    },
    {
      Name: "United Kingdom",
      Id: 3
    },
    {
      Name: "Spain",
      Id: 4
    },
    {
      Name: "Mexico",
      Id: 5
    }
  ],
  valueField: "Id",
  textField: "Name",
};





// select and search box js //
function dropdown() {
  return {
    options: [],
    selected: [],
    show: false,
    open() {
      this.show = true
    },
    close() {
      this.show = false
    },
    isOpen() {
      return this.show === true
    },
    select(index, event) {

      if (!this.options[index].selected) {

        this.options[index].selected = true;
        this.options[index].element = event.target;
        this.selected.push(index);

      } else {
        this.selected.splice(this.selected.lastIndexOf(index), 1);
        this.options[index].selected = false
      }
    },
    remove(index, option) {
      this.options[option].selected = false;
      this.selected.splice(index, 1);
    },
    loadOptions() {
      const options = document.getElementById('select').options;
      for (let i = 0; i < options.length; i++) {
        this.options.push({
          value: options[i].value,
          text: options[i].innerText,
          selected: options[i].getAttribute('selected') != null ? options[i].getAttribute('selected') : false
        });
      }
    },
    selectedValues() {
      return this.selected.map((option) => {
        return this.options[option].value;
      })
    }
  }
}




// file upload browser js //

(function ($) {
  'use strict';
  $(function () {
    $('.file-upload-browse').on('click', function () {
      var file = $(this).parent().parent().parent().find('.file-upload-default');
      file.trigger('click');
    });
    $('.file-upload-default').on('change', function () {
      $(this).parent().find('.form-control').val($(this).val().replace(/C:\\fakepath\\/i, ''));
    });
  });
})(jQuery);




//form-repeter //
function addFormField() {
  var id = document.getElementById("id").value;

  $("#divTxt").append(
    "<p id='row" +
    id +
    "'><label for='txt" +
    id +
    "'>" +
    id +
    "&nbsp;&nbsp;<input type='file' size='80' name='txt[]' id='txt' class='form-control addrow'" +
    id +
    "'>&nbsp;&nbsp<a href='#' class='btn-danger' onClick='removeFormField(\"#row" +
    id +
    "\"); return false;'><i class='fa-regular fa-trash-can'></i></a><p>"
  );

  id = id - 1 + 2;
  document.getElementById("id").value = id;
}

function removeFormField(id) {
  $(id).remove();
}



// CKEDITOR //

CKEDITOR.replace('editor1');
CKEDITOR.on('instanceReady', function (evt) {
  var editor = evt.editor;

  editor.on('change', function (e) {
    var contentSpace = editor.ui.space('contents');
    var ckeditorFrameCollection = contentSpace.$.getElementsByTagName('iframe');
    var ckeditorFrame = ckeditorFrameCollection[0];
    var innerDoc = ckeditorFrame.contentDocument;
    var innerDocTextAreaHeight = $(innerDoc.body).height();
    console.log(innerDocTextAreaHeight);
  });
});