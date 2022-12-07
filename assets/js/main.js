const validImageTypes = ['image/jpg', 'image/jpeg', 'image/png']

function upload(){
    var files = $('#upload-button').prop('files')
    if (files.length == 0) {
        $('#upload-status').text("Please select an image")
    } else{
        var file = files[0]
        var file_name = file.name
        var file_type = file['type']
        var form_data = new FormData()
        form_data.append("file", file)
        
        console.log(file)
        console.log(file_name)
        console.log(file_type)

        if (!validImageTypes.includes(file_type)) {
            $('#upload-status').text("Not an image. Upload files ending with .jpg, .jpeg, or .png")
        } else {
            var reader = new FileReader();
            var params = {
                'x-amz-meta-userid': "adi",
                'x-amz-meta-language': "de",
                "Content-Type" : "image/jpeg"
            }
            reader.onload = function(event) {
                const file =  new Uint8Array(event.target.result)
                file.constructor = () => file;
                sdk.uploadPost(
                    params, file, {} 
                ).then(function(result){
                    console.log(result)
                    $('#upload-status').text("Upload is successful")
                }).catch(function(result){
                    console.log(result)
                    $('#upload-status').text("Upload is error")
                })
            };
            reader.readAsArrayBuffer(file);
        }
    }
}

$( document ).ready(function() {
    console.log('Start');
    $("#submit-button").click(function(event) {
        upload();
    })
    $("#upload-button").click(function(event) {
        console.log("New File Requested")
        $('#upload-status').text("");
    })
})