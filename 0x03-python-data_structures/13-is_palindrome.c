#include "lists.h"

/**
 * is_palindrome - check if a linekd list is a palindrome
 * @head: pointer to pointer to the first node
 * Return: 0 if it is not a palidrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int palindrome, first, len, last;
	listint_t *first_node, *last_node, *current;

	palindrome = 1;
	len = get_length(*head);
	if (*head == NULL || len == 1)
		return (palindrome);
	last = len;
	first = 1;
	first_node = *head;
	last_node = *head;
	while (last_node->next != NULL)
		last_node = last_node->next;
	while (first < last && palindrome)
	{
		if (first_node->n != last_node->n)
			palindrome = 0;
		first++;
		last--;
		first_node = first_node->next;
		current = *head;
		while (current->next != last_node)
			current = current->next;
		last_node = current;
	}
	return (palindrome);
}

/**
 * get_length - get length of a linked list
 * @head: head node
 * Return: length of the linked list or 0 if none
 */

int get_length(listint_t *head)
{
	int count;

	count = 0;
	if (head == NULL)
		return (0);
	while (head != NULL)
	{
		count++;
		head = head->next;
	}
	return (count);
}
