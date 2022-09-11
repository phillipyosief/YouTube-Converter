console.log('[i] Request.js loaded');

document.addEventListener('DOMContentLoaded', function() {
    var DownloadAsMP3 = document.getElementById('DownloadAsMP3');
    var DownloadAsMP4 = document.getElementById('DownloadAsMP4');
    var GitHubRepo = document.getElementById('GitHubRepo');
    var Bugreport = document.getElementById('Bugreport');
    var Donate = document.getElementById('Donate');

    DownloadAsMP4.addEventListener('click', function() {
        chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
        function(tabs){
            console.log('[i] DownloadAsMP4 clicked');
            var currenturl = tabs[0].url
      
            fetch('http://localhost:5000/YouTube/convert', {
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
      
            fetch('http://localhost:5000/YouTube/convert', {
              method: "GET",
              headers: {"url": currenturl,
                        "type": "mp3"}
      
            })
            .then(response => response.json())
            .then(json => console.log(json))
            .catch(err => console.log(err));
        });
    }, false);

    Bugreport.addEventListener('click', function() {
        console.log('[i] Bugreport clicked');
        chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
        function(tabs){
            fetch('http://localhost:5000/web/bugreport', {
              method: "GET"
            })
            .then(response => response.json())
            .then(json => console.log(json))
            .catch(err => console.log(err));
        });
    }, false);

    GitHubRepo.addEventListener('click', function() {
        console.log('[i] GitHubRepo clicked');
        open('https://github.com/philliphqs/YouTube-Converter');
    }, false);

    Donate.addEventListener('click', function() {
        console.log('[i] Donate clicked');
        open('https://buymeacoffee.com/phillip.hqs');
    }, false);
})


