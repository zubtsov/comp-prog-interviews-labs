function solveDuplicatedNumberMistake(arr) {
    let numberExists = new Array(arr.length + 1).fill(false);
    let duplicatedNumber;

    for (let i = 0; i < arr.length; i++) {
        let currentNumber = arr[i];
        if (!numberExists[currentNumber]) {
            numberExists[currentNumber] = true;
        } else {
            duplicatedNumber = currentNumber;
        }
    }

    for (let i = 1; i < numberExists.length; i++) {
        if (!numberExists[i]) {
            let missingNumber = i;
            return duplicatedNumber + missingNumber;
        }
    }
}