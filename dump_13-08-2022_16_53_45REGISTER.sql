--
-- PostgreSQL database cluster dump
--

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Drop databases (except postgres and template1)
--

DROP DATABASE ticketing_db;




--
-- Drop roles
--

DROP ROLE postgres;


--
-- Roles
--

CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'md52a03a42547969c3d6d642a33470f3cd5';






--
-- Databases
--

--
-- Database "template1" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 13.7 (Debian 13.7-1.pgdg110+1)
-- Dumped by pg_dump version 13.7 (Debian 13.7-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

UPDATE pg_catalog.pg_database SET datistemplate = false WHERE datname = 'template1';
DROP DATABASE template1;
--
-- Name: template1; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE template1 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE template1 OWNER TO postgres;

\connect template1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE template1; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE template1 IS 'default template for new databases';


--
-- Name: template1; Type: DATABASE PROPERTIES; Schema: -; Owner: postgres
--

ALTER DATABASE template1 IS_TEMPLATE = true;


\connect template1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE template1; Type: ACL; Schema: -; Owner: postgres
--

REVOKE CONNECT,TEMPORARY ON DATABASE template1 FROM PUBLIC;
GRANT CONNECT ON DATABASE template1 TO PUBLIC;


--
-- PostgreSQL database dump complete
--

--
-- Database "postgres" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 13.7 (Debian 13.7-1.pgdg110+1)
-- Dumped by pg_dump version 13.7 (Debian 13.7-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE postgres;
--
-- Name: postgres; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE postgres OWNER TO postgres;

\connect postgres

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: DATABASE postgres; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- PostgreSQL database dump complete
--

--
-- Database "ticketing_db" dump
--

--
-- PostgreSQL database dump
--

-- Dumped from database version 13.7 (Debian 13.7-1.pgdg110+1)
-- Dumped by pg_dump version 13.7 (Debian 13.7-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: ticketing_db; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE ticketing_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE ticketing_db OWNER TO postgres;

\connect ticketing_db

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: ticket_app_correspondence; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ticket_app_correspondence (
    id bigint NOT NULL,
    description character varying(1000) NOT NULL,
    date_creation timestamp with time zone NOT NULL,
    user_id bigint NOT NULL,
    ticket_correspondence_id bigint NOT NULL
);


ALTER TABLE public.ticket_app_correspondence OWNER TO postgres;

--
-- Name: ticket_app_correspondence_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ticket_app_correspondence_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ticket_app_correspondence_id_seq OWNER TO postgres;

--
-- Name: ticket_app_correspondence_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ticket_app_correspondence_id_seq OWNED BY public.ticket_app_correspondence.id;


--
-- Name: ticket_app_department; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ticket_app_department (
    id bigint NOT NULL,
    name_department character varying(64) NOT NULL,
    desc_department character varying(255) NOT NULL
);


ALTER TABLE public.ticket_app_department OWNER TO postgres;

--
-- Name: ticket_app_department_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ticket_app_department_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ticket_app_department_id_seq OWNER TO postgres;

--
-- Name: ticket_app_department_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ticket_app_department_id_seq OWNED BY public.ticket_app_department.id;


--
-- Name: ticket_app_departmentproblem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ticket_app_departmentproblem (
    id bigint NOT NULL,
    category_problem character varying(64) NOT NULL,
    department_id bigint NOT NULL
);


ALTER TABLE public.ticket_app_departmentproblem OWNER TO postgres;

--
-- Name: ticket_app_departmentproblem_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ticket_app_departmentproblem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ticket_app_departmentproblem_id_seq OWNER TO postgres;

--
-- Name: ticket_app_departmentproblem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ticket_app_departmentproblem_id_seq OWNED BY public.ticket_app_departmentproblem.id;


--
-- Name: ticket_app_historyticket; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ticket_app_historyticket (
    id bigint NOT NULL,
    description character varying(255) NOT NULL,
    date_creation timestamp with time zone NOT NULL
);


ALTER TABLE public.ticket_app_historyticket OWNER TO postgres;

--
-- Name: ticket_app_historyticket_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ticket_app_historyticket_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ticket_app_historyticket_id_seq OWNER TO postgres;

--
-- Name: ticket_app_historyticket_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ticket_app_historyticket_id_seq OWNED BY public.ticket_app_historyticket.id;


--
-- Name: ticket_app_ticket; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ticket_app_ticket (
    id bigint NOT NULL,
    title character varying(64) NOT NULL,
    description text NOT NULL,
    priorytet character varying(64) NOT NULL,
    date_creation timestamp with time zone,
    date_resolve timestamp with time zone,
    department_assignment_id bigint NOT NULL,
    status character varying(64) NOT NULL,
    user_requestor_id bigint NOT NULL,
    problem_category_id bigint NOT NULL,
    date_update timestamp with time zone NOT NULL
);


ALTER TABLE public.ticket_app_ticket OWNER TO postgres;

--
-- Name: ticket_app_ticket_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ticket_app_ticket_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ticket_app_ticket_id_seq OWNER TO postgres;

--
-- Name: ticket_app_ticket_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ticket_app_ticket_id_seq OWNED BY public.ticket_app_ticket.id;


--
-- Name: ticket_app_ticket_user_assignment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ticket_app_ticket_user_assignment (
    id bigint NOT NULL,
    ticket_id bigint NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.ticket_app_ticket_user_assignment OWNER TO postgres;

--
-- Name: ticket_app_ticket_user_assignment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ticket_app_ticket_user_assignment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ticket_app_ticket_user_assignment_id_seq OWNER TO postgres;

--
-- Name: ticket_app_ticket_user_assignment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ticket_app_ticket_user_assignment_id_seq OWNED BY public.ticket_app_ticket_user_assignment.id;


--
-- Name: ticket_app_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ticket_app_user (
    id bigint NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    address_city character varying(64) NOT NULL,
    phone_number integer NOT NULL,
    department_id bigint NOT NULL,
    is_email_verified boolean NOT NULL
);


ALTER TABLE public.ticket_app_user OWNER TO postgres;

--
-- Name: ticket_app_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ticket_app_user_groups (
    id bigint NOT NULL,
    user_id bigint NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.ticket_app_user_groups OWNER TO postgres;

--
-- Name: ticket_app_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ticket_app_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ticket_app_user_groups_id_seq OWNER TO postgres;

--
-- Name: ticket_app_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ticket_app_user_groups_id_seq OWNED BY public.ticket_app_user_groups.id;


--
-- Name: ticket_app_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ticket_app_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ticket_app_user_id_seq OWNER TO postgres;

--
-- Name: ticket_app_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ticket_app_user_id_seq OWNED BY public.ticket_app_user.id;


--
-- Name: ticket_app_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ticket_app_user_user_permissions (
    id bigint NOT NULL,
    user_id bigint NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.ticket_app_user_user_permissions OWNER TO postgres;

--
-- Name: ticket_app_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ticket_app_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ticket_app_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: ticket_app_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ticket_app_user_user_permissions_id_seq OWNED BY public.ticket_app_user_user_permissions.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: ticket_app_correspondence id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_correspondence ALTER COLUMN id SET DEFAULT nextval('public.ticket_app_correspondence_id_seq'::regclass);


--
-- Name: ticket_app_department id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_department ALTER COLUMN id SET DEFAULT nextval('public.ticket_app_department_id_seq'::regclass);


--
-- Name: ticket_app_departmentproblem id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_departmentproblem ALTER COLUMN id SET DEFAULT nextval('public.ticket_app_departmentproblem_id_seq'::regclass);


--
-- Name: ticket_app_historyticket id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_historyticket ALTER COLUMN id SET DEFAULT nextval('public.ticket_app_historyticket_id_seq'::regclass);


--
-- Name: ticket_app_ticket id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_ticket ALTER COLUMN id SET DEFAULT nextval('public.ticket_app_ticket_id_seq'::regclass);


--
-- Name: ticket_app_ticket_user_assignment id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_ticket_user_assignment ALTER COLUMN id SET DEFAULT nextval('public.ticket_app_ticket_user_assignment_id_seq'::regclass);


--
-- Name: ticket_app_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_user ALTER COLUMN id SET DEFAULT nextval('public.ticket_app_user_id_seq'::regclass);


--
-- Name: ticket_app_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_user_groups ALTER COLUMN id SET DEFAULT nextval('public.ticket_app_user_groups_id_seq'::regclass);


--
-- Name: ticket_app_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.ticket_app_user_user_permissions_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add user	6	add_user
22	Can change user	6	change_user
23	Can delete user	6	delete_user
24	Can view user	6	view_user
25	Can add correspondence	7	add_correspondence
26	Can change correspondence	7	change_correspondence
27	Can delete correspondence	7	delete_correspondence
28	Can view correspondence	7	view_correspondence
29	Can add department	8	add_department
30	Can change department	8	change_department
31	Can delete department	8	delete_department
32	Can view department	8	view_department
33	Can add department problem	9	add_departmentproblem
34	Can change department problem	9	change_departmentproblem
35	Can delete department problem	9	delete_departmentproblem
36	Can view department problem	9	view_departmentproblem
37	Can add history ticket	10	add_historyticket
38	Can change history ticket	10	change_historyticket
39	Can delete history ticket	10	delete_historyticket
40	Can view history ticket	10	view_historyticket
41	Can add status	11	add_status
42	Can change status	11	change_status
43	Can delete status	11	delete_status
44	Can view status	11	view_status
45	Can add ticket	12	add_ticket
46	Can change ticket	12	change_ticket
47	Can delete ticket	12	delete_ticket
48	Can view ticket	12	view_ticket
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	ticket_app	user
7	ticket_app	correspondence
8	ticket_app	department
9	ticket_app	departmentproblem
10	ticket_app	historyticket
11	ticket_app	status
12	ticket_app	ticket
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2021-09-04 10:14:49.281259+00
2	contenttypes	0002_remove_content_type_name	2021-09-04 10:14:49.288279+00
3	auth	0001_initial	2021-09-04 10:14:49.318093+00
4	auth	0002_alter_permission_name_max_length	2021-09-04 10:14:49.322702+00
5	auth	0003_alter_user_email_max_length	2021-09-04 10:14:49.326787+00
6	auth	0004_alter_user_username_opts	2021-09-04 10:14:49.331054+00
7	auth	0005_alter_user_last_login_null	2021-09-04 10:14:49.335918+00
8	auth	0006_require_contenttypes_0002	2021-09-04 10:14:49.337654+00
9	auth	0007_alter_validators_add_error_messages	2021-09-04 10:14:49.34186+00
10	auth	0008_alter_user_username_max_length	2021-09-04 10:14:49.347196+00
11	auth	0009_alter_user_last_name_max_length	2021-09-04 10:14:49.351313+00
12	auth	0010_alter_group_name_max_length	2021-09-04 10:14:49.356023+00
13	auth	0011_update_proxy_permissions	2021-09-04 10:14:49.359982+00
14	auth	0012_alter_user_first_name_max_length	2021-09-04 10:14:49.363875+00
15	ticket_app	0001_initial	2021-09-04 10:14:49.44237+00
16	admin	0001_initial	2021-09-04 10:14:49.459054+00
17	admin	0002_logentry_remove_auto_add	2021-09-04 10:14:49.46661+00
18	admin	0003_logentry_add_action_flag_choices	2021-09-04 10:14:49.474661+00
19	sessions	0001_initial	2021-09-04 10:14:49.482575+00
20	ticket_app	0002_auto_20210904_1027	2021-09-04 10:27:44.09079+00
21	ticket_app	0003_alter_ticket_correspondence	2021-09-04 10:31:23.93443+00
22	ticket_app	0004_alter_ticket_user_requestor	2021-09-04 10:31:23.944156+00
23	ticket_app	0005_auto_20210904_1255	2021-09-04 12:56:33.962661+00
24	ticket_app	0006_auto_20210904_1301	2021-09-04 13:01:09.663134+00
25	ticket_app	0007_auto_20210904_1311	2021-09-04 13:11:42.626825+00
26	ticket_app	0008_alter_ticket_description	2021-09-04 14:28:30.003032+00
27	ticket_app	0009_auto_20210904_1430	2021-09-04 14:30:24.835861+00
28	ticket_app	0010_auto_20210904_1441	2021-09-05 08:34:59.766444+00
29	ticket_app	0011_alter_departmentproblem_department	2021-09-05 08:34:59.796424+00
30	ticket_app	0012_auto_20210904_1527	2021-09-05 08:37:26.229495+00
31	ticket_app	0013_alter_ticket_date_resolve	2021-09-05 08:37:26.24249+00
32	ticket_app	0014_alter_ticket_date_resolve	2021-09-05 08:37:26.254879+00
33	ticket_app	0015_auto_20210904_1637	2021-09-05 08:37:26.280636+00
34	ticket_app	0016_alter_ticket_date_resolve	2021-09-05 08:37:26.293401+00
35	ticket_app	0017_alter_ticket_date_resolve	2021-09-05 08:37:26.306082+00
36	ticket_app	0018_auto_20210905_0906	2021-09-05 09:06:29.006236+00
37	ticket_app	0019_alter_user_department	2021-09-05 10:19:59.919074+00
38	ticket_app	0020_alter_ticket_date_resolve	2021-09-05 17:14:51.011173+00
39	ticket_app	0021_alter_ticket_date_resolve	2021-09-05 17:15:56.051844+00
40	ticket_app	0022_alter_ticket_date_resolve	2021-09-05 17:19:10.048816+00
41	ticket_app	0023_alter_ticket_date_update	2021-09-11 04:10:51.395677+00
42	ticket_app	0024_alter_ticket_date_update	2021-09-11 04:10:51.42744+00
43	ticket_app	0025_alter_ticket_date_creation	2021-09-11 04:10:51.44881+00
44	ticket_app	0026_auto_20210906_0921	2021-09-11 04:10:51.546332+00
45	ticket_app	0027_alter_ticket_status	2021-09-11 04:10:51.586441+00
46	ticket_app	0028_alter_ticket_date_creation	2021-09-11 04:10:51.616263+00
47	ticket_app	0029_alter_ticket_date_creation	2021-09-11 04:10:51.653251+00
48	ticket_app	0030_alter_ticket_date_creation	2021-09-11 04:10:51.697673+00
49	ticket_app	0031_alter_ticket_date_creation	2021-09-11 04:10:51.733737+00
50	ticket_app	0032_alter_ticket_date_creation	2021-09-11 04:10:51.757314+00
51	ticket_app	0033_auto_20210907_1011	2021-09-11 04:10:51.814068+00
52	ticket_app	0034_alter_ticket_date_creation	2021-09-11 06:56:53.454777+00
53	ticket_app	0035_alter_ticket_date_creation	2021-09-11 07:02:41.203857+00
54	ticket_app	0002_auto_20220813_1423	2022-08-13 14:31:10.103504+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
zqxkcunt610wtb5r61v7snwviw5er62l	e30:1mP3wP:N_qmSrRquOr_wgLavhpNi7Sqjc_MaDsOCasyFBiWYl0	2021-09-25 14:25:13.891555+00
hed4fxte1x674svxlmdx5p6ibvp28vsp	.eJxVjDsOwjAQBe_iGlkJ_q0p6TmDteu1cQDZUpxUiLuTSCmgfTPz3iLgupSw9jSHicVFjOL0uxHGZ6o74AfWe5Ox1WWeSO6KPGiXt8bpdT3cv4OCvWz1AFExW2PAQbLas7IqGg9Ag3JEmi2PFhJkdJmyNnT2ZPxGmCNkj-LzBdkFOGE:1mP6Gu:ZkUs6mVavjLVmUTo1RNXrj6LJyc-TqYnJamZ6xIuv4A	2021-09-25 16:54:32.825522+00
\.


--
-- Data for Name: ticket_app_correspondence; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ticket_app_correspondence (id, description, date_creation, user_id, ticket_correspondence_id) FROM stdin;
1	What problem do you have, please specify	2021-09-11 09:39:51.25078+00	2	20
2	asdas	2021-09-11 15:26:32.145417+00	5	1
3	sdgfdsg	2021-09-11 16:54:05.65438+00	6	11
4	dfhdgfh	2021-09-11 16:54:55.628518+00	1	11
5	sfdg	2021-09-11 16:55:10.356196+00	1	11
\.


--
-- Data for Name: ticket_app_department; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ticket_app_department (id, name_department, desc_department) FROM stdin;
1	Test	Department Test
2	IT	Information Technology
3	HR	Human Resources
4	PM	Project Management
5	FB	Finance & Buyers 
\.


--
-- Data for Name: ticket_app_departmentproblem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ticket_app_departmentproblem (id, category_problem, department_id) FROM stdin;
2	Desktops/Software	2
3	Pherieral devices	2
4	Mobile Devices	2
5	Network/Infrastructure	2
6	Work Schedule	3
7	Hiring Process	3
8	Employee	3
9	Documents	3
10	Project realization	4
11	Improvement	4
12	Inspection	4
13	Invoices	5
14	Payment	5
15	Delegation payment	5
16	Orders	5
\.


--
-- Data for Name: ticket_app_historyticket; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ticket_app_historyticket (id, description, date_creation) FROM stdin;
\.


--
-- Data for Name: ticket_app_ticket; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ticket_app_ticket (id, title, description, priorytet, date_creation, date_resolve, department_assignment_id, status, user_requestor_id, problem_category_id, date_update) FROM stdin;
1	SOme HR Problem4	Discription of Ticket. J Have some problem with laptopAAAAAAAAAAAAaa	Medium	2021-09-05 10:28:46.955+00	2021-09-05 10:28:48.238+00	3	Dropped	11	9	2021-09-11 08:46:04.645116+00
21	Computer Problem 3	JACEK	Low	2021-09-11 06:48:43.034239+00	\N	2	Work in Progress	2	5	2021-09-11 06:49:17.791664+00
20	Computer Problem 1	fgfdgdfgdfg	Low	2021-09-11 06:46:09.506049+00	\N	2	Blocked	7	4	2021-09-11 06:46:26.342953+00
24	SOme HR Problem3	fdgdfdfgsdfsdf	Medium	2021-09-11 06:55:05.111645+00	\N	3	Not Acknowledged	5	7	2021-09-11 06:55:55.148177+00
8	Project Problem 5	JACEK	Low	2021-09-11 06:48:43.034239+00	\N	4	Work in Progress	1	10	2021-09-11 06:49:17.791664+00
6	Project Problem 3	VBBBBBBBBBBBBBBBBBb	High	2021-09-11 06:17:56.543592+00	\N	4	Not Acknowledged	11	12	2021-09-11 06:17:57.071727+00
19	Computer Problem 2	VBBBBBBBBBBBBBBBBBb	High	2021-09-11 06:17:56.543592+00	\N	2	Not Acknowledged	9	3	2021-09-11 06:17:57.071727+00
22	Computer Problem 4	gfdgdfg	Low	2021-09-11 06:53:39.514992+00	\N	2	Not Acknowledged	8	2	2021-09-11 06:53:57.58452+00
17	Computer Problem 5	sdfsdfsdfsdfsdfzzAAAAAAAAAAAAAAAAAAAAAAAA	Low	2021-09-05 09:26:19.380797+00	2021-09-05 09:26:19.380832+00	2	Resolved Successfull 	12	2	2021-09-11 05:02:12.363153+00
2	Project Problem 1	sdfsdfsdfsdfsdfzzAAAAAAAAAAAAAAAAAAAAAAAA	Low	2021-09-05 09:26:19.380797+00	2021-09-05 09:26:19.380832+00	4	Resolved Successfull	7	2	2021-09-11 05:02:12.363153+00
5	SOme HR Problem1	EDIT	Medium	2021-09-11 06:23:23.52986+00	\N	3	Pending Requestor Information	12	7	2021-09-11 10:15:38.559419+00
62	Computer problem	Laptop problem	Low	2021-09-11 10:22:20.224506+00	\N	2	Not Acknowledged	5	2	2021-09-11 10:22:41.234406+00
7	Project Problem 4	fgfdgdfgdfg	Low	2021-09-11 06:46:09.506049+00	\N	4	Blocked	6	11	2021-09-11 15:08:56.086229+00
18	SOme HR Problem5	sdfsdfsdfsdfsdf	Low	2021-09-11 05:05:01.686335+00	\N	3	Not Acknowledged	6	8	2021-09-11 15:14:45.584741+00
23	SOme HR Problem6	egdfg	Low	2021-09-11 06:55:05.111645+00	\N	3	Not Acknowledged	6	6	2021-09-11 15:15:04.942391+00
4	Computer Problem 6	description	Low	2021-09-11 05:33:45.132808+00	\N	2	Not Acknowledged	11	2	2021-09-11 15:16:25.331505+00
61	SOme HR Problem2	DDDDDDDDDDDD	Low	2021-09-11 06:55:05.111645+00	\N	3	Not Acknowledged	2	6	2021-09-11 17:02:33.935156+00
3	Project Problem 2	description	Low	2021-09-11 05:33:45.132808+00	\N	4	Not Acknowledged	10	11	2021-09-11 17:02:54.935204+00
9	Order Product problem 1	gfdgdfg	Low	2021-09-11 06:53:39.514992+00	\N	5	Not Acknowledged	1	13	2021-09-11 06:53:57.58452+00
14	Order Product problem 5	Discription of Ticket. J Have some problem with laptopAAAAAAAAAAAAaa	Medium	2021-09-05 10:28:46.955+00	2021-09-05 10:28:48.238+00	5	Dropped	6	15	2021-09-11 08:46:04.645116+00
11	Order Product problem 3	fdgdfdfgsdfsdf	Medium	2021-09-11 06:55:05.111645+00	\N	5	Not Acknowledged	3	15	2021-09-11 06:55:55.148177+00
15	Order Product problem 2	EDIT	Medium	2021-09-11 06:23:23.52986+00	\N	5	Pending Requestor Information	10	13	2021-09-11 09:35:01.597333+00
13	Project Problem 6	sdfsdfsdfsdfsdf	Low	2021-09-11 05:05:01.686335+00	\N	4	Not Acknowledged	5	10	2021-09-11 08:45:10.18368+00
10	Order Product problem 4	egdfg	Low	2021-09-11 06:55:05.111645+00	\N	5	Not Acknowledged	2	14	2021-09-11 06:55:17.226645+00
12	Order Product problem 6	DDDDDDDDDDDD	Low	2021-09-11 06:55:05.111645+00	\N	5	Not Acknowledged	4	16	2021-09-11 07:02:47.219551+00
\.


--
-- Data for Name: ticket_app_ticket_user_assignment; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ticket_app_ticket_user_assignment (id, ticket_id, user_id) FROM stdin;
49	19	2
50	19	3
51	19	4
68	20	3
69	21	1
70	21	6
71	22	2
73	24	1
74	24	6
76	1	3
77	5	2
78	5	11
79	5	7
80	62	1
83	7	8
84	7	3
85	18	2
86	18	7
87	4	6
88	3	12
\.


--
-- Data for Name: ticket_app_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ticket_app_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, address_city, phone_number, department_id, is_email_verified) FROM stdin;
5	pbkdf2_sha256$260000$f8c3oXeiUbUmP8PjjHFDpC$0if/IPzOy3FmrmOKrZ6Y1GDpvsj6DOlwDznEgNtvOiQ=	\N	f	fb_ania	Ania	FB_Surname	fb@admin.com	t	t	2021-09-04 10:23:37.824659+00	Szczecin	444444444	5	f
2	pbkdf2_sha256$260000$f8c3oXeiUbUmP8PjjHFDpC$0if/IPzOy3FmrmOKrZ6Y1GDpvsj6DOlwDznEgNtvOiQ=	\N	f	hr_kasia	Kasia	HR_Surname	hr@admin.com	t	t	2021-09-04 10:23:37.824659+00	Szczecin	222222222	3	f
3	pbkdf2_sha256$260000$f8c3oXeiUbUmP8PjjHFDpC$0if/IPzOy3FmrmOKrZ6Y1GDpvsj6DOlwDznEgNtvOiQ=	\N	f	pm_andrzej	Andrzej	PM_Surname	pm@admin.com	t	t	2021-09-04 10:23:37.824659+00	Szczecin	333333333	4	f
7	pbkdf2_sha256$260000$f8c3oXeiUbUmP8PjjHFDpC$0if/IPzOy3FmrmOKrZ6Y1GDpvsj6DOlwDznEgNtvOiQ=	\N	f	hr_magda	Magda	HR_Surname	hr@admin.com	t	t	2021-09-04 10:23:37.824659+00	Szczecin	222222222	3	f
8	pbkdf2_sha256$260000$f8c3oXeiUbUmP8PjjHFDpC$0if/IPzOy3FmrmOKrZ6Y1GDpvsj6DOlwDznEgNtvOiQ=	\N	f	pm_kacper	Kacper	PM_Surname	pm@admin.com	t	t	2021-09-04 10:23:37.824659+00	Szczecin	333333333	4	f
9	pbkdf2_sha256$260000$f8c3oXeiUbUmP8PjjHFDpC$0if/IPzOy3FmrmOKrZ6Y1GDpvsj6DOlwDznEgNtvOiQ=	\N	f	fb_paweł	Paweł	FB_Surname	fb@admin.com	t	t	2021-09-04 10:23:37.824659+00	Szczecin	444444444	5	f
10	pbkdf2_sha256$260000$f8c3oXeiUbUmP8PjjHFDpC$0if/IPzOy3FmrmOKrZ6Y1GDpvsj6DOlwDznEgNtvOiQ=	\N	f	it_krzysztof	Krzysztof	IT_Surname	it@admin.com	t	t	2021-09-04 10:23:37.824659+00	Szczecin	111111111	2	f
11	pbkdf2_sha256$260000$f8c3oXeiUbUmP8PjjHFDpC$0if/IPzOy3FmrmOKrZ6Y1GDpvsj6DOlwDznEgNtvOiQ=	\N	f	hr_paulina	Paulina	HR_Surname	hr@admin.com	t	t	2021-09-04 10:23:37.824659+00	Szczecin	222222222	3	f
12	pbkdf2_sha256$260000$f8c3oXeiUbUmP8PjjHFDpC$0if/IPzOy3FmrmOKrZ6Y1GDpvsj6DOlwDznEgNtvOiQ=	\N	f	pm_grzegorz	Grzegorz	PM_Surname	pm@admin.com	t	t	2021-09-04 10:23:37.824659+00	Szczecin	333333333	4	f
4	pbkdf2_sha256$260000$f8c3oXeiUbUmP8PjjHFDpC$0if/IPzOy3FmrmOKrZ6Y1GDpvsj6DOlwDznEgNtvOiQ=	2021-09-11 14:31:39.736769+00	t	admin			admin@admin.com	t	t	2021-09-04 10:23:37.824659+00	N/A	0	1	f
6	pbkdf2_sha256$260000$f8c3oXeiUbUmP8PjjHFDpC$0if/IPzOy3FmrmOKrZ6Y1GDpvsj6DOlwDznEgNtvOiQ=	2021-09-11 16:50:28.801229+00	f	it_jacek	Jacek	IT_Surname	it@admin.com	t	t	2021-09-04 10:23:37.824659+00	Szczecin	111111111	2	f
1	pbkdf2_sha256$260000$f8c3oXeiUbUmP8PjjHFDpC$0if/IPzOy3FmrmOKrZ6Y1GDpvsj6DOlwDznEgNtvOiQ=	2021-09-11 16:54:32.823414+00	f	it_bartek	InforName	IT_Surname	it@admin.com	t	t	2021-09-04 10:23:37.824659+00	Szczecin	111111111	2	f
\.


--
-- Data for Name: ticket_app_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ticket_app_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: ticket_app_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ticket_app_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 48, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 12, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 54, true);


--
-- Name: ticket_app_correspondence_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ticket_app_correspondence_id_seq', 5, true);


--
-- Name: ticket_app_department_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ticket_app_department_id_seq', 5, true);


--
-- Name: ticket_app_departmentproblem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ticket_app_departmentproblem_id_seq', 16, true);


--
-- Name: ticket_app_historyticket_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ticket_app_historyticket_id_seq', 1, false);


--
-- Name: ticket_app_ticket_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ticket_app_ticket_id_seq', 62, true);


--
-- Name: ticket_app_ticket_user_assignment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ticket_app_ticket_user_assignment_id_seq', 88, true);


--
-- Name: ticket_app_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ticket_app_user_groups_id_seq', 1, false);


--
-- Name: ticket_app_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ticket_app_user_id_seq', 16, true);


--
-- Name: ticket_app_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ticket_app_user_user_permissions_id_seq', 1, false);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: ticket_app_correspondence ticket_app_correspondence_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_correspondence
    ADD CONSTRAINT ticket_app_correspondence_pkey PRIMARY KEY (id);


--
-- Name: ticket_app_department ticket_app_department_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_department
    ADD CONSTRAINT ticket_app_department_pkey PRIMARY KEY (id);


--
-- Name: ticket_app_departmentproblem ticket_app_departmentproblem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_departmentproblem
    ADD CONSTRAINT ticket_app_departmentproblem_pkey PRIMARY KEY (id);


--
-- Name: ticket_app_historyticket ticket_app_historyticket_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_historyticket
    ADD CONSTRAINT ticket_app_historyticket_pkey PRIMARY KEY (id);


--
-- Name: ticket_app_ticket ticket_app_ticket_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_ticket
    ADD CONSTRAINT ticket_app_ticket_pkey PRIMARY KEY (id);


--
-- Name: ticket_app_ticket_user_assignment ticket_app_ticket_user_a_ticket_id_user_id_f67eaa29_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_ticket_user_assignment
    ADD CONSTRAINT ticket_app_ticket_user_a_ticket_id_user_id_f67eaa29_uniq UNIQUE (ticket_id, user_id);


--
-- Name: ticket_app_ticket_user_assignment ticket_app_ticket_user_assignment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_ticket_user_assignment
    ADD CONSTRAINT ticket_app_ticket_user_assignment_pkey PRIMARY KEY (id);


--
-- Name: ticket_app_user_groups ticket_app_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_user_groups
    ADD CONSTRAINT ticket_app_user_groups_pkey PRIMARY KEY (id);


--
-- Name: ticket_app_user_groups ticket_app_user_groups_user_id_group_id_17320698_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_user_groups
    ADD CONSTRAINT ticket_app_user_groups_user_id_group_id_17320698_uniq UNIQUE (user_id, group_id);


--
-- Name: ticket_app_user ticket_app_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_user
    ADD CONSTRAINT ticket_app_user_pkey PRIMARY KEY (id);


--
-- Name: ticket_app_user_user_permissions ticket_app_user_user_per_user_id_permission_id_aa39a7d0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_user_user_permissions
    ADD CONSTRAINT ticket_app_user_user_per_user_id_permission_id_aa39a7d0_uniq UNIQUE (user_id, permission_id);


--
-- Name: ticket_app_user_user_permissions ticket_app_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_user_user_permissions
    ADD CONSTRAINT ticket_app_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: ticket_app_user ticket_app_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_user
    ADD CONSTRAINT ticket_app_user_username_key UNIQUE (username);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: ticket_app_correspondence_ticket_correspondence_id_dab7194b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ticket_app_correspondence_ticket_correspondence_id_dab7194b ON public.ticket_app_correspondence USING btree (ticket_correspondence_id);


--
-- Name: ticket_app_correspondence_user_id_fe0ea71e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ticket_app_correspondence_user_id_fe0ea71e ON public.ticket_app_correspondence USING btree (user_id);


--
-- Name: ticket_app_departmentproblem_department_id_e194d448; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ticket_app_departmentproblem_department_id_e194d448 ON public.ticket_app_departmentproblem USING btree (department_id);


--
-- Name: ticket_app_ticket_department_assignment_id_7a607196; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ticket_app_ticket_department_assignment_id_7a607196 ON public.ticket_app_ticket USING btree (department_assignment_id);


--
-- Name: ticket_app_ticket_problem_category_id_bf798beb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ticket_app_ticket_problem_category_id_bf798beb ON public.ticket_app_ticket USING btree (problem_category_id);


--
-- Name: ticket_app_ticket_user_assignment_ticket_id_b99e2cd4; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ticket_app_ticket_user_assignment_ticket_id_b99e2cd4 ON public.ticket_app_ticket_user_assignment USING btree (ticket_id);


--
-- Name: ticket_app_ticket_user_assignment_user_id_2b125c5f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ticket_app_ticket_user_assignment_user_id_2b125c5f ON public.ticket_app_ticket_user_assignment USING btree (user_id);


--
-- Name: ticket_app_ticket_user_requestor_id_aef8bf5d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ticket_app_ticket_user_requestor_id_aef8bf5d ON public.ticket_app_ticket USING btree (user_requestor_id);


--
-- Name: ticket_app_user_department_id_e394c7c2; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ticket_app_user_department_id_e394c7c2 ON public.ticket_app_user USING btree (department_id);


--
-- Name: ticket_app_user_groups_group_id_c6a9cd69; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ticket_app_user_groups_group_id_c6a9cd69 ON public.ticket_app_user_groups USING btree (group_id);


--
-- Name: ticket_app_user_groups_user_id_e7ba3fa7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ticket_app_user_groups_user_id_e7ba3fa7 ON public.ticket_app_user_groups USING btree (user_id);


--
-- Name: ticket_app_user_user_permissions_permission_id_99ef5519; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ticket_app_user_user_permissions_permission_id_99ef5519 ON public.ticket_app_user_user_permissions USING btree (permission_id);


--
-- Name: ticket_app_user_user_permissions_user_id_aa0d73cf; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ticket_app_user_user_permissions_user_id_aa0d73cf ON public.ticket_app_user_user_permissions USING btree (user_id);


--
-- Name: ticket_app_user_username_7bd2db80_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ticket_app_user_username_7bd2db80_like ON public.ticket_app_user USING btree (username varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk FOREIGN KEY (user_id) REFERENCES public.ticket_app_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ticket_app_correspondence ticket_app_correspondence_ticket_correspondence_id_dab7194b_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_correspondence
    ADD CONSTRAINT ticket_app_correspondence_ticket_correspondence_id_dab7194b_fk FOREIGN KEY (ticket_correspondence_id) REFERENCES public.ticket_app_ticket(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ticket_app_correspondence ticket_app_correspondence_user_id_fe0ea71e_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_correspondence
    ADD CONSTRAINT ticket_app_correspondence_user_id_fe0ea71e_fk FOREIGN KEY (user_id) REFERENCES public.ticket_app_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ticket_app_departmentproblem ticket_app_departmentproblem_department_id_e194d448_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_departmentproblem
    ADD CONSTRAINT ticket_app_departmentproblem_department_id_e194d448_fk FOREIGN KEY (department_id) REFERENCES public.ticket_app_department(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ticket_app_ticket ticket_app_ticket_department_assignment_id_7a607196_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_ticket
    ADD CONSTRAINT ticket_app_ticket_department_assignment_id_7a607196_fk FOREIGN KEY (department_assignment_id) REFERENCES public.ticket_app_department(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ticket_app_ticket ticket_app_ticket_problem_category_id_bf798beb_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_ticket
    ADD CONSTRAINT ticket_app_ticket_problem_category_id_bf798beb_fk FOREIGN KEY (problem_category_id) REFERENCES public.ticket_app_departmentproblem(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ticket_app_ticket ticket_app_ticket_user_requestor_id_aef8bf5d_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_ticket
    ADD CONSTRAINT ticket_app_ticket_user_requestor_id_aef8bf5d_fk FOREIGN KEY (user_requestor_id) REFERENCES public.ticket_app_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ticket_app_user ticket_app_user_department_id_e394c7c2_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_user
    ADD CONSTRAINT ticket_app_user_department_id_e394c7c2_fk FOREIGN KEY (department_id) REFERENCES public.ticket_app_department(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ticket_app_user_groups ticket_app_user_groups_group_id_c6a9cd69_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_user_groups
    ADD CONSTRAINT ticket_app_user_groups_group_id_c6a9cd69_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ticket_app_user_user_permissions ticket_app_user_user_permission_id_99ef5519_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ticket_app_user_user_permissions
    ADD CONSTRAINT ticket_app_user_user_permission_id_99ef5519_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

--
-- PostgreSQL database cluster dump complete
--

