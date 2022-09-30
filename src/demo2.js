class Person {
    /**
     * Creates a person
     *
     * @param {string} name The person`s full name
     * @param {num} age The person`s age
     * @param {boolean} IsDeveloper Whether or not the person is a developer
     */
    constructor(name, age, IsDeveloper) {
        this.name = name;
        this.age = age;
        this.IsDeveloper = IsDeveloper;
    }
}

/**
 * Gives you numbers.
 *
 * @returns {number[]}
 */
function getNumbers() {
    return [10, 80, 130, 150]
}


const numbers = getNumbers();
