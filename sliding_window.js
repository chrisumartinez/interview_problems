const findSubArrays = (inputArr, desiredSum) => {
	// current window sum and window sum start index
	let sum = 0;
	let sumStartIndex = 0;
	const solutions = [];

	inputArr.forEach((item, index) => {
		sum += item;

		while (sum > desiredSum) {
			sum -= inputArr[sumStartIndex];
			sumStartIndex++;
		}

		if (sum === desiredSum) {
			solutions.push(
				inputArr.filter((_, i) => i >= sumStartIndex && i <= index)
			);
		}
	});

	return solutions;
};
// Variation: Given an array of integers (negative, 0, positive), find the subarrays that add up to
//  given Number.
const kadaneAlgo = (inputArr, desiredSum) => {
	let currSum = 0;
	let left = 0;
	let right = 0;
	let result = [];

	inputArr.forEach((item, index) => {
		currSum += item;
		right += 1;

		if (currSum == desiredSum) {
			result.push(inputArr.slice(left, right));
			currSum = 0;
			left = index + 1;
			right = left;
		}
		if (currSum < 0) {
			currSum = 0;
			left = index + 1;
			right = left;
		}

		console.log("iteration: ", index);
		console.log("currSum: ", currSum);
		console.log("Array: ", result);

		console.log("");
	});

	console.log("Left: ", left);
	console.log("Right: ", right);
	console.log("Array: ", result);

	return result;
};

const exampleInput1 = [1, 7, 9, 4, 3, 2, 2];
const exampleInput2 = [-1, 4, -7, 3, 1, 1, 5, -9, 2, 7];
const desiredSum2 = 5;
const desiredSum1 = 7;

//console.log(findSubArrays(exampleInput1, desiredSum1));
console.log(kadaneAlgo(exampleInput2, desiredSum2));
