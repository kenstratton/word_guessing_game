(() => {

    // Provide the popup of game help
    var help = document.getElementById('help')
    var popup = document.getElementById('help-popup');
    help.addEventListener('click', () => {
        popup.classList.toggle('show') });


    // Execute when the game page is accessed
    if (document.getElementsByClassName('game')){

        // Reveal characters in a secret word
        const reveal_sec = key => {
            Array.from(document.getElementsByClassName(`sec-${key}`))
                .filter(function(c){c.className = 'revealed'});
            char_lis_len -= 1 };

        // Change the status of soil-to-ufo parameter
        const alt_up = () => {
            bar_num-=1;
            var bar = document.getElementsByTagName('td')[bar_num];
            bar.classList.add('up') };

        // Prohibit an elemnt from pointer events
        const not_allowed = (element) => {
            element.classList.add('not-allowed') };

        // Provide the popup of game result
        const result_popup = (result) => {
            var popup = document.getElementsByClassName('popup')[0]
            var popup_content = popup.children[0]
            var play_link = popup.children[1]
            popup_content.textContent = (result) ? 'Correct!': 'Game Over';
            play_link.textContent = (result) ? 'NEXT GAME': 'PLAY AGAIN';
            popup.style.visibility = 'visible' };

        // Check if guessing is accurate
        const verdict = () => {
            if (char_lis_len == 0 || bar_num == 0) {
                var game_body = document.getElementsByClassName('game')[0]
                not_allowed(game_body)
                result = (char_lis_len == 0) ? true: false;
                result_popup(result)} };

        // If a key has been not used, disable the key and return TRUE
        // Otherwise, return FALSE
        const check_key = key => {
            var key_obj = document.getElementById(key);
            if (key_obj && key_obj.className != 'used') {
                key_obj.className = 'used';
                return true 
            } else {return false} };

        // Event by input of an alphabet character
        const input_event = key => {
            if (result == null && check_key(key)) {
                if (char_lis.includes(key)) {
                    reveal_sec(key)
                } else {alt_up()}; 
                verdict()} };


        //  Tells game has been done without having null
        var result = null;

        // Define a list cantains characters in a secret word and its length
        var char_lis = [];

        var slots = (document.getElementsByClassName('slot'));
        for (let i = 0; i < slots.length; i++) {
            var char = slots[i].children[0].textContent;
            if (!char_lis.includes(char)) {char_lis.push(char)} };

        var char_lis_len = char_lis.length

        // Create a soil-to-ufo bar and insert into HTML
        var bar_num = (char_lis_len > 7) ? 5+(char_lis_len-7): 5;
        var bar_html = `<tr><td style='height:${275/bar_num}px;'></td></tr>`;
        var alt_bar = document.getElementsByClassName('alt-bar')[0];

        for (let i = 0; i < bar_num; i++) {
             alt_bar.insertAdjacentHTML('afterbegin', bar_html) };


        // Get a keybord input and link to an event
        document.addEventListener('keydown',
            event => {
                var key = event.key.toUpperCase();
                input_event(key)} );

        // Get a click input and link to an event
        Array.from(document.getElementsByClassName('usable'))
            .filter( alph => {
                alph.addEventListener('click', () => {
                    var key = alph.textContent;
                    input_event(key)}); });
    };
})();