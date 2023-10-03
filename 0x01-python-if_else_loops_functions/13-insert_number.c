#include "lists.h"

/**
 * insert_node - insert a node to a sorted list
 * @head: pointer to the head node pointer
 * @number: new node data
 * Return: The address of the new node or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *tmp;

	node = (listint_t *)malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;
	if (*head == NULL || (*head)->n > number)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	tmp = *head;
	while (tmp->next != NULL) /* while i've not reach the last node */
	{
		if (number > tmp->n && number < tmp->next->n)
		{
			node->next = tmp->next;
			tmp->next = node;
			return (node);
		}
		tmp = tmp->next;
	}
	tmp->next = node;
	return (node);
}
