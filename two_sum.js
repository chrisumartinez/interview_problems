const twoSum = (nums, target) => {
	const ht = {};
	let result = [];
	nums.forEach((item, index) => {
		const complement = target - item;
		if (complement in ht) {
			//console.log("complement: ", complement, " index: ", index);
			result = [ht[complement], index];
		}
		ht[item] = index;
		//console.log("ht: ", ht);
	});
	return result;
};

const nums = [2, 7, 11, 15];
const target = 9;
console.log(twoSum(nums, target));
