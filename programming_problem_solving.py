"""Examples of turning a problem into small, composable functions."""


def sum_even(numbers: list[int]) -> int:
    return sum(number for number in numbers if number % 2 == 0)


def maximum(numbers: list[int]) -> int:
    if not numbers:
        raise ValueError('maximum needs at least one number')
    return max(numbers)


def parse_numbers(text: str) -> list[int]:
    """Convert comma-separated input into integers with useful errors."""
    try:
        return [int(part.strip()) for part in text.split(',') if part.strip()]
    except ValueError as error:
        raise ValueError('input must contain comma-separated integers') from error


if __name__ == '__main__':
    numbers = parse_numbers('1, 2, 3, 4, 5, 6')
    print({'numbers': numbers, 'sum_even': sum_even(numbers), 'maximum': maximum(numbers)})
