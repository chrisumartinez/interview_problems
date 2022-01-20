const isValid = (s) => {
	stack = [];
	const arr = s.split("");
    const flag = false;
	arr.forEach((item) => {
		console.log("stack b4: ", stack);
		console.log("item: ", item);
		if (stack.length === 0) {
			stack.push(item);
		} else {
			if (item === ")") {
				if (stack[stack.length - 1] === "(") {
					stack.pop();
				}
			} else {
				if (item === "}") {
					if (stack[stack.length - 1] === "{") {
						stack.pop();
					} else {
						return false;
                    
					}
				} else {
					if (item === "]") {
						if (stack[stack.length - 1] === "[") {
							stack.pop();
						} else {
							return false;
                            
						}
					} else {
						stack.push(item);
					}
				}
			}
		}
		console.log("stack after: ", stack);
		console.log();
	});
	if (stack.length === 0) {
		return true;
	} else {
		return false;
	}
};

const str = "(])";
console.log(isValid(str));
