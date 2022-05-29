window.onload = () => {
  $("#sendbutton").click(() => {
    imagebox = $("#imagebox");
    link = $("#link");
    input = $("#imageinput")[0];
    labelmap = $("#labelmap")[0];
    console.log(labelmap);
    console.log(imagebox);
    console.log(link);
    console.log(input);
    if (input.files && input.files[0]) {
      let formData = new FormData();
      formData.append("video", input.files[0]);
      // formData.append("class_names",labelmap.files[0]);
      console.log(input.files[0]);
      $.ajax({
        url: "/detect", // fix this to your liking
        type: "POST",
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        error: function (data) {
          console.log("upload error", data);
          console.log(data.getAllResponseHeaders());
        },
        success: function (data) {
          console.log(data);
          // bytestring = data["status"];
          // image = bytestring.split("'")[1];
          $("#link").css("visibility", "visible");
          $("#download").attr("href", "static/" + data); 
          console.log(data);
        },
      });
    }
  });
};

function readUrl(input) {
  imagebox = $("#imagebox");
  console.log("image box is",imagebox);
  console.log("input is",input)
  console.log("evoked readUrl");
  console.log(input.files)
  console.log("input files [0]",input.files[0])
  if (input.files && input.files[0]) {
    let reader = new FileReader();
    reader.onload = function (e) {
      console.log(e.target);

      imagebox.attr("src", e.target.result);
      //   imagebox.height(500);
      //   imagebox.width(800);
    };
    reader.readAsDataURL(input.files[0]);
  }
}
