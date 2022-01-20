const palindrome = (s) => {
	const regex = /[^A-Za-z0-9]/g;
	const newStr = s.replace(regex, "").toLowerCase();
	const reversedStr = newStr.split("").reverse("").join("");

	// console.log("string: ", newStr);
	// console.log("reversedStr: ", reversedStr);
	if (newStr === reversedStr) {
		return true;
	} else {
		return false;
	}
};

const sentence = "A man, a plan, a canal: Panama";
console.log(palindrome(sentence));
const s = "race a car";
console.log(palindrome(s));
