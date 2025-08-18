CREATE TABLE [dbo].[app_menu] (

	[Id] int NULL, 
	[menu_name] varchar(60) NULL, 
	[menu_link] varchar(255) NULL, 
	[menu_path] varchar(255) NULL, 
	[menu_need_approval] varchar(3) NULL, 
	[menu_icon] varchar(60) NULL, 
	[menu_parent] int NULL, 
	[create_at] datetime2(6) NULL, 
	[modify_at] datetime2(6) NULL, 
	[created_by] int NULL, 
	[modified_by] int NULL
);