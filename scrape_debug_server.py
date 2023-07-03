from flask import Flask
from flask import request
from flask import render_template
from werkzeug.datastructures import ImmutableMultiDict, EnvironHeaders
import pprint

app = Flask(__name__)

def get_output():
    # Narrowd down to the props I think are the most useful
    props = sorted(set([
        # "_cached_json",
        # "_get_file_stream",
        # "_get_stream_for_parsing",
        # "_load_form_data",
        # "_parse_content_type",
        # "accept_charsets",
        "accept_encodings",
        "accept_languages",
        "accept_mimetypes",
        # "access_control_request_headers",
        # "access_control_request_method",
        "access_route",
        # "application",
        # "args",
        # "authorization",
        "base_url",
        # "blueprint",
        # "blueprints",
        "cache_control",
        "charset",
        # "close",
        # "content_encoding",
        # "content_length",
        # "content_md5",
        # "content_type",
        "cookies",
        "data",
        # "date",
        # "dict_storage_class",
        # "encoding_errors",
        # "endpoint",
        "environ",
        # "files",
        # "form",
        # "form_data_parser_class",
        # "from_values",
        "full_path",
        # "get_data",
        # "get_json",
        "headers",
        "host",
        "host_url",
        # "if_match",
        # "if_modified_since",
        # "if_none_match",
        # "if_range",
        # "if_unmodified_since",
        # "input_stream",
        # "is_json",
        # "is_multiprocess",
        # "is_multithread",
        # "is_run_once",
        "is_secure",
        # "json",
        # "json_module",
        # "list_storage_class",
        # "make_form_data_parser",
        # "max_content_length",
        # "max_form_memory_size",
        # "max_forwards",
        "method",
        # "mimetype",
        # "mimetype_params",
        # "on_json_loading_failed",
        # "origin",
        # "parameter_storage_class",
        "path",
        # "pragma",
        "query_string",
        # "range",
        "referrer",
        "remote_addr",
        "remote_user",
        "root_path",
        "root_url",
        # "routing_exception",
        "scheme",
        # "script_root",
        "server",
        # "shallow",
        # "stream",
        # "trusted_hosts",
        "url",
        "url_charset",
        "url_root",
        # "url_rule",
        # "user_agent",
        # "user_agent_class",
        "values",
        # "view_args",
        # "want_form_data_parsed",
    ]))

    output = {}
    for p in props:
        try:
            out = getattr(request, p)

            if isinstance(out, ImmutableMultiDict) or isinstance(out, EnvironHeaders):
                out = { k: out.getlist(k) for k in out.keys() }

            output[p] = {
                "type": f"{'.'.join([type(out).__module__, type(out).__qualname__])}",
                "value": f"""{pprint.pformat(out)}""",
                "status": True,
            }

        except Exception as e:
            output[p] = {
                "type": str(type(e)),
                "value": str(e),
                "status": False,
            }

    return output


@app.route("/")
def human_readable():
    # Code styling comes from here: https://stackoverflow.com/a/48694906
    return render_template('human_readable.html', output = get_output())

@app.route("/json")
def machine_readable():
    return get_output()
