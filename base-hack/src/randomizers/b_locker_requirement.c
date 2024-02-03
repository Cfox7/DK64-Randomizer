#include "../../include/common.h"

void setBLockerHead(void) {
    int item = 0;
    int world = getWorld(CurrentMap, 0);
    if (world <= 7) {
        item = Rando.b_locker_requirements[world].item;
    }
    blink(CurrentActorPointer_0, 3, 1);
    applyImageToActor(CurrentActorPointer_0, 3, 0);
    adjustColorPalette(CurrentActorPointer_0, 3, item, 0.0f);
    unkPaletteFunc(CurrentActorPointer_0, 3, 0);
}

void displayBlockerItemOnHUD(void) {
    setBLockerHead();
    int world = getWorld(CurrentMap, 0);
    if (world > 7) {
        return;
    }
    if (Rando.b_locker_requirements[world].item == REQITEM_GOLDENBANANA) {
        displayItemOnHUD(9, 1, 0);
    }
}

int getCountOfBlockerRequiredItem(void) {
    int world = getWorld(CurrentMap, 0);
    if (world > 7) {
        return 0;
    }
    return getItemCountReq(Rando.b_locker_requirements[world].item);
}

void initBLocker(void) {
    writeFunction(0x80027570, &displayBlockerItemOnHUD);
    writeFunction(0x800279D0, &getCountOfBlockerRequiredItem);
    writeFunction(0x8002792C, &getCountOfBlockerRequiredItem);
}