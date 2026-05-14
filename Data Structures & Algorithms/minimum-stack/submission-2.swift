class MinStack {

    init() {
        self.stack = [Int]()
        self.minStack = [Int]()
    }

    var stack: [Int]
    var minStack: [Int]

    func push(_ val: Int) {
        stack.append(val)
        minStack.append(min(minStack.last ?? Int.max, val))
    }

    func pop() {
        var _ = stack.popLast() ?? 1
        var _ = minStack.popLast() ?? 1
    }

    func top() -> Int {
        return stack.last ?? 0
    }

    func getMin() -> Int {
        return minStack.last ?? 0
    }
}
