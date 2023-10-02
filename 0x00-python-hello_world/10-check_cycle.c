#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - check if a linked list is a circular linked list
 * @list: pointer a head of a linked list
 * Return: 0 - no cycle, 1 - cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *head;

	if (list == NULL)
		return (0);
	head = list;
	while (list != NULL && list->next != head)
		list = list->next;
	if (list == NULL)
		return (0);
	if (list->next == head)
		return (1);
	return (0);
}
