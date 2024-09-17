/**
 * @file music_text.c
 * @author Ballaam
 * @brief Display the name of a song on the bottom of the screen when played
 * @version 0.1
 * @date 2024-03-25
 * 
 * @copyright Copyright (c) 2024
 * 
 */

#include "../../include/common.h"

static unsigned char display_timer = 0;
static short displayed_text_offset = -1;
static int currently_stored_sequence[4] = {0, 0, 0, 0};
static int last_known_cseqp_state[4] = {0, 0, 0, 0};  // Only storing 1 for playing and 0 for not playing.

void resetDisplayedMusic(void) {
    DisplayedSongNamePointer = 0; // Uses a static address for autotrackers
}

void initSongDisplay(){
    int seq_player = 0;
    int sequence = 0;
    int state = 0;

    for(int i = 0; i < 4; i++){
        seq_player = compactSequencePlayers[i];
        sequence = cspGetSequence(seq_player);
        
        if(sequence != currently_stored_sequence[i]){
            currently_stored_sequence[i] = sequence;
            last_known_cseqp_state[i] = 0;  // In case it stopped and started within a videoFrame
        }
        if(last_known_cseqp_state[i] == 0){
            state = cspGetState(seq_player);
            if(state == 1){
                newSongPlays(sequenceToSongIndex(sequence));
            }
        }
    }
}

void newSongPlays(int song) {
    if (song == 0) {
        return;
    }
    if (song == 34) {
        // Block it from occurring in the pause menu, cause text overload
        return;
    }
    if (music_types[song] != SONGTYPE_BGM) {
        return;
    }
    if ((CurrentMap == MAP_ISLES) && (CutsceneActive == 1) && (CutsceneIndex == 29)) {
        // In K Rool gets launched cutscene
        return;
    }
    if (DisplayedSongNamePointer) {
        complex_free(DisplayedSongNamePointer);
    }
    DisplayedSongNamePointer = getTextPointer(46, song, 0);
    displayed_text_offset = -1;
    int text_length = cstring_strlen(DisplayedSongNamePointer);
    display_timer = 60;
    if (ObjectModel2Timer < 31) {
        display_timer += 31;
    }
    for (int i = 0; i < text_length; i++) {
        if (DisplayedSongNamePointer[i] == 0xA) {
            DisplayedSongNamePointer[i] = 0;
            displayed_text_offset = i + 1;
        }
    }
}

int cspGetSequence(int seqp){

}

int sequenceToSongIndex(int sequence){
//This function is impossible
}

Gfx* displaySongNameHandler(Gfx* dl) {
    if ((!Rando.show_music_name) || (display_timer == 0)) {
        return dl;
    }
    if (display_timer > 0) {
        display_timer -= 1;
    }
    if (!DisplayedSongNamePointer) {
        return dl;
    }
    if (displayed_text_offset == -1) {
        return dl;
    }
    for (int i = 0; i < 2; i++) {
        mtx_item mtx0;
        mtx_item mtx1;
        _guScaleF(&mtx0, 0x3F19999A, 0x3F19999A, 0x3F800000);
        _guTranslateF(&mtx1, 50.0f, 800.0f + (i * 30.0f), 0.0f);
        _guMtxCatF(&mtx0, &mtx1, &mtx0);
        _guTranslateF(&mtx1, 0.0f, 48.0f, 0.0f);
        _guMtxCatF(&mtx0, &mtx1, &mtx0);
        _guMtxF2L(&mtx0, &static_mtx[20 + i]);

        gSPDisplayList(dl++, 0x01000118);
        gSPMatrix(dl++, 0x02000180, G_MTX_PUSH | G_MTX_LOAD | G_MTX_MODELVIEW);
        gDPPipeSync(dl++);
        gDPSetCombineLERP(dl++, 0, 0, 0, TEXEL0, TEXEL0, 0, PRIMITIVE, 0, 0, 0, 0, TEXEL0, TEXEL0, 0, PRIMITIVE, 0);
        gDPSetPrimColor(dl++, 0, 0, 0xFF, 0xFF, 0xFF, 0xFF);
        gSPMatrix(dl++, (int)&static_mtx[20 + i], G_MTX_PUSH | G_MTX_LOAD | G_MTX_MODELVIEW);
        dl = displayText(dl,6,0,0,DisplayedSongNamePointer + (displayed_text_offset * i),0);
        gSPPopMatrix(dl++, G_MTX_MODELVIEW);
    }
    return dl;
}