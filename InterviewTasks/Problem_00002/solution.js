function isLastTileReachable(arr) {
    let currentTileIndex = 0;
    let lastTileIndex = arr.length - 1;
    let stepsRemained = arr[0];

    while (currentTileIndex < lastTileIndex && stepsRemained > 0) {
        currentTileIndex++;
        stepsRemained--;
        if (arr[currentTileIndex] > stepsRemained) {
            stepsRemained = arr[currentTileIndex];
        }
    }

    return (currentTileIndex === lastTileIndex);
}