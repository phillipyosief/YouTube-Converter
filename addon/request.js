console.log('[i] Request.js loaded');

document.addEventListener('DOMContentLoaded', function() {
    var DownloadAsMP3 = document.getElementById('DownloadAsMP3');
    var DownloadAsMP4 = document.getElementById('DownloadAsMP4');

    DownloadAsMP4.addEventListener('click', function() {
        chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
        function(tabs){
            console.log('[i] DownloadAsMP4 clicked');
            var currenturl = tabs[0].url
      
            fetch('http://localhost:2222/YouTube/convert', {
              method: "GET",
              headers: {"url": currenturl,
                        "type": "mp4"}
      
            })
            .then(response => response.json())
            .then(json => console.log(json))
            .catch(err => console.log(err));
        });
    }, false);


    DownloadAsMP3.addEventListener('click', function() {
        console.log('[i] DownloadAsMP3 clicked');
        chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
        function(tabs){
            console.log('[i] DownloadAsMP3 clicked');
            var currenturl = tabs[0].url
      
            fetch('http://localhost:2222/YouTube/convert', {
              method: "GET",
              headers: {"url": currenturl,
                        "type": "mp3"}
      
            })
            .then(response => response.json())
            .then(json => console.log(json))
            .catch(err => console.log(err));
        });
    }, false);
})


function DownloadAsMP4() {
    console.log('[i] DownloadAsMP4 clicked');
    chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
    function(tabs){
        console.log('[i] DownloadAsMP4 clicked');
        var currenturl = tabs[0].url
  
        fetch('http://localhost:2222/YouTube/convert', {
          method: "GET",
          headers: {"url": currenturl,
                    "type": "mp4"}
  
        })
        .then(response => response.json())
        .then(json => console.log(json))
        .catch(err => console.log(err));
    });
}

function DownloadAsMP3() {
    console.log('[i] DownloadAsMP3 clicked');
    chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
    function(tabs){
        console.log('[i] DownloadAsMP3 clicked');
        var currenturl = tabs[0].url
  
        fetch('http://localhost:2222/YouTube/convert', {
          method: "GET",
          headers: {"url": currenturl,
                    "type": "mp3"}
  
        })
        .then(response => response.json())
        .then(json => console.log(json))
        .catch(err => console.log(err));
    });
}