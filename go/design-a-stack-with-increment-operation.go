type CustomStack struct {
	MaxSize    int
	Stack      []int
	Increments []int
}

func Constructor(maxSize int) CustomStack {
	// Initialize CustomStack object
	customStack := CustomStack{
		MaxSize:    maxSize,
		Stack:      make([]int, 0),
		Increments: make([]int, 0),
	}
	return customStack
}

func (this *CustomStack) Push(x int) {
	if len(this.Stack) < this.MaxSize {
		// Add element to the stack
		this.Stack = append(this.Stack, x)
		// Add an increment of 0 to the increment's stack
		this.Increments = append(this.Increments, 0)
	}
}

func (this *CustomStack) Pop() int {
	n := len(this.Stack)
	if 0 < n {
		// Pop increment, rollover to the lower level
		increment := this.Increments[n-1]
		this.Increments = this.Increments[:n-1]
		this.Increment(len(this.Increments), increment)
		// Pop element from stack
		peak := this.Stack[n-1]
		this.Stack = this.Stack[:n-1]
		// Return the stack value and the increment
		return peak + increment
	} else {
		return -1
	}
}

func (this *CustomStack) Increment(k int, val int) {
	n := len(this.Increments)
	if 0 < n {
		// Pick smallest from Increment stack size and k
		minimal_index := k
		if n < minimal_index {
			minimal_index = n
		}
		// Update increment in the position of the stack
		this.Increments[minimal_index-1] += val
	}
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * obj := Constructor(maxSize);
 * obj.Push(x);
 * param_2 := obj.Pop();
 * obj.Increment(k,val);
 */
