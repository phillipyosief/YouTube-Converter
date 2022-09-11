console.log('[i] Request.js loaded');




document.addEventListener('DOMContentLoaded', function() {
    var DownloadAsMP3 = document.getElementById('DownloadAsMP3');
    var DownloadAsMP4 = document.getElementById('DownloadAsMP4');
    var GitHubRepo = document.getElementById('GitHubRepo');
    var Bugreport = document.getElementById('Bugreport');
    var Donate = document.getElementById('Donate');

    DownloadAsMP4.addEventListener('click', function() {
        // get current browser url
        browser.tabs.query({active: true, currentWindow: true}).then(function(tabs) {
            var url = tabs[0].url;
            console.log('[i] Current URL: ' + url);

            console.log('[i] DownloadAsMP4 clicked');

            resp = fetch('http://127.0.0.1:5000/YouTube/convert', {
            method: "GET",
            headers: {"url": url,
                      "type": "mp4"}});
        });
    }, false);

    
    DownloadAsMP3.addEventListener('click', function() {
        // get current browser url
        browser.tabs.query({active: true, currentWindow: true}).then(function(tabs) {
            var url = tabs[0].url;
            console.log('[i] Current URL: ' + url);

            console.log('[i] DownloadAsMP3 clicked');

            resp = fetch('http://127.0.0.1:5000/YouTube/convert', {
            method: "GET",
            headers: {"url": url,
                      "type": "mp3"}});
        });
    }, false);

    Bugreport.addEventListener('click', function() {
        console.log('[i] Bugreport clicked');

        fetch('http://127.0.0.1:5000/web/bugreport', {
          method: "GET"
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


