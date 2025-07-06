export interface TProfile {
	key: number,
	name: string,
	bio?: string,
	avatarUrl?: string,
	isOnline: boolean,
}

export interface TMovie {
	key: number,
	name: string
	director: string
	genre: string
}


export interface Task {
	id: number,
	name: string,
	descreption: string,
	priority: string,
}


export enum TaskPriority {
	High = "high",
	Medium = "medium",
	Low = "low"
}

export interface ITask {
	id: string,
	name: string,
	description?: string,
	priority: TaskPriority
	created_at: Date,
	updated_at: Date
}

export interface ITaskCreate {
	name: string,
	description?: string,
	priority: TaskPriority
}
