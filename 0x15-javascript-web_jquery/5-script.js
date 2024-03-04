$(document).ready(function () {
  $('DIV#add_item').click(function () {
    const liElement = $('<li>').text('Item');
    console.log(liElement);
    $('UL.my_list').append(liElement);
  });
});
